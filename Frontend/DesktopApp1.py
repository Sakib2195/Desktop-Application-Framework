from os import path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout, QDialog, QMessageBox
from FinalUI import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QCoreApplication
from pm4py.visualization.dfg import visualizer as dfg_visualization
import glob
import sys
import os
import pandas as pd
from pm4py.objects.log.importer.xes import importer as xes_importer
import os, shutil
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.importer import importer as pnml_importer
from dockermanager import DockerManager
import json
from PyQt5 import QtCore, QtWidgets
import pickle
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtCore import *

class FirstApp(Ui_MainWindow):
    def __init__(self,window):

        
        
        self.setupUi(window)
        
        self.direcname= " "
        self.tabWidget.setCurrentIndex(0)
        self.buttonSelectDocker.setEnabled(False)
        self.buttonApplyAlgorithm.setEnabled(False)
        self.buttonDisplay.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonImportlog.clicked.connect(self.logload)
        self.buttonApplyAlgorithm.clicked.connect(self.run_algorithm)
        self.buttonSelectDocker.clicked.connect(self.selectLog)
        self.buttonExport.clicked.connect(self.exportFiles)
        self.buttonExit.clicked.connect(self.ExitApp)
        self.buttonDisplay.clicked.connect(self.displayOutput)

        self.dest = ''
        self.direcname =''
        self.tabWidget.setTabEnabled(2,False);
        dock_manager = DockerManager()
        
        algorithms_list = dock_manager.list_algorithms()["repositories"]
        for algo in algorithms_list:
            self.listAlgorithm.addItem(algo)

        self.listAlgorithm.clicked.connect(self.algo_item_clicked)   
        # MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        # enable custom window hint
        MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint)

# disable (but not hide) close button
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
    
        
        
    
        
    def logload(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        filename=QtWidgets.QFileDialog.getOpenFileName(None, "Window name", "", "XES files (*.xes)")
        self.direcname = filename[0]
        self.log_name = QFileInfo(self.direcname).fileName()
        print(self.log_name)
        if self.direcname != '':
            if os.stat(self.direcname).st_size == 0:
                print("empty file!")
                msgBox = QMessageBox()
                msgBox.setText("Empty File,Please import another file!")
                msgBox.exec()
            else :   
                self.listImportedLog.addItem(self.log_name)
                self.buttonSelectDocker.setEnabled(True)
                self.input_path = config["PATHS"]["VOLUME_PATH_MAC"]+"input_files/"
                shutil.copy(self.direcname,self.input_path)
        elif self.direcname == '':
                print("Choose a File")
                

            
            
        self.log_name_selected = " "
        self.listImportedLog.clicked.connect(self.log_item_clicked)
        

    
    def ExitApp(self):
        with open('config.json', 'r') as f:
            config = json.load(f)

        filelist_INPUT = glob.glob(os.path.join(self.input_path, "*"))
        for f in filelist_INPUT:
            os.remove(f)
        
        filelist_output_data = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'alpha_miner/output_data/', "*"))
        for f in filelist_output_data:
            os.remove(f)
        filelist_output_data1 = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'dfg/output_data/', "*"))
        for f in filelist_output_data1:
            os.remove(f)
        filelist_output_data2 = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'heuristic_miner/output_data/', "*"))
        for f in filelist_output_data2:
            os.remove(f)
        filelist_output_data3 = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'inductive_miner/output_data/', "*"))
        for f in filelist_output_data3:
            os.remove(f)
        
        filelist_input_data = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'alpha_miner/input_data/', "*"))
        for f in filelist_input_data:
            os.remove(f)
        filelist_input_data1 = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'dfg/input_data/', "*"))
        for f in filelist_input_data1:
            os.remove(f)
        filelist_input_data2 = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'heuristic_miner/input_data/', "*"))
        for f in filelist_input_data2:
            os.remove(f)
        filelist_input_data3 = glob.glob(os.path.join(config["PATHS"]["VOLUME_PATH_MAC"]+'inductive_miner/input_data/', "*"))
        for f in filelist_input_data3:
            os.remove(f)
        
        MainWindow.close()


    def exportFiles(self):
    
        self.completeName = self.output_path
        print("Complete name",self.completeName)
        fn= QFileDialog.getSaveFileName(caption='Export File')
        self.dest=fn[0]
        
        files_output = os.listdir(self.completeName)
        print(self.dest)

        for file in files_output:
            if self.dest != '':
                ab=shutil.copy(self.completeName+file,self.dest)
            elif self.dest == '':
                print("No Path Selected")

    def displayOutput(self):
        
        print("3)")
        print(self.log_name_selected)
        if ".pnml" in self.log_name_selected:
            print("4")
            print("input path",self.input_path+self.log_name_selected)
            net, initial_marking, final_marking = pnml_importer.apply(self.input_path+self.log_name_selected)
            gviz = pn_visualizer.apply(net, initial_marking, final_marking)
            pn_visualizer.view(gviz)
            print("5")
        elif ".pickle" in self.log_name_selected:
            print("input path pickle",self.input_path+self.log_name_selected)
            with open(self.input_path+self.log_name_selected, 'rb') as inputfile:
                
                print("input file",inputfile)
                log_direc = xes_importer.apply(self.input_file_path)
                output = pickle.load(inputfile)
                print("self input file path",self.input_file_path)
                parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "png"}
                gviz = dfg_visualization.apply(output, log=log_direc, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)
                dfg_visualization.view(gviz)
            
        else:
            msgBox = QMessageBox()
            msgBox.setText("Select a petrinet or a .pickle file!")
            msgBox.exec()
            

            
                
                
    def log_item_clicked(self):

        item1 =self.listImportedLog.currentItem()
        self.log_name_selected = str(item1.text())        
        print("selected current log is",self.log_name_selected)

    
    def algo_item_clicked(self):

        item =self.listAlgorithm.currentItem()
        self.algo_name_selected = str(item.text())
        print("The selected current item is",self.algo_name_selected)
        self.buttonApplyAlgorithm.setEnabled(True)
        
        with open('config.json','r') as f:
            config = json.load(f)
       
        
        if self.algo_name_selected == "alpha_miner":
            self.label_showAlgoSummary.setText("INPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['ALPHA_MINER']['INPUT'])+"\nOUTPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['ALPHA_MINER']['OUTPUT'])+"\nDESCRIPTION:\n"+"".join(config['ALGORITHMS']['ALPHA_MINER']['DESCRIPTION']))
        elif self.algo_name_selected == "inductive_miner":
              self.label_showAlgoSummary.setText("INPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['INDUCTIVE_MINER']['INPUT'])+"\nOUTPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['INDUCTIVE_MINER']['OUTPUT'])+"\nDESCRIPTION:\n"+"".join(config['ALGORITHMS']['INDUCTIVE_MINER']['DESCRIPTION']))
        elif self.algo_name_selected == "heuristic_miner":
              self.label_showAlgoSummary.setText("INPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['HEURISTIC_MINER']['INPUT'])+"\nOUTPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['HEURISTIC_MINER']['OUTPUT'])+"\nDESCRIPTION:\n"+"".join(config['ALGORITHMS']['HEURISTIC_MINER']['DESCRIPTION']))
        elif self.algo_name_selected == "dfg":
               self.label_showAlgoSummary.setText("INPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['DFG']['INPUT'])+"\nOUTPUT PARAMETERS:\n"+"".join(config['ALGORITHMS']['DFG']['OUTPUT'])+"\nDESCRIPTION:\n"+"".join(config['ALGORITHMS']['DFG']['DESCRIPTION']))
        
            
    def showLogSummary(self):
        log = xes_importer.apply(self.direcname)
        print(log[0])
        self.labelLogSummary.setText(str(log[0]))
        self.labelLogSummary.setWordWrap(True)

    def selectLog(self):
        if ".xes" in self.log_name_selected:
            self.tabWidget.setCurrentIndex(1)
            self.buttonApplyAlgorithm.setEnabled(False)
            
            
            print("selected_log_name",self.log_name_selected)
            self.input_file_path = self.input_path+self.log_name_selected
            print("INPUT File Path",self.input_file_path)

        elif self.log_name_selected == " ":
            
            msgBox = QMessageBox()
            msgBox.setText("Select a .xes file format!")
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setText("Select a .xes file format!")
            msgBox.exec()

    
    def run_algorithm(self):
        with open('config.json', 'r') as f:
            config = json.load(f)


        print("selected algorithm is",self.algo_name_selected) 
        self.algo_input_path = config["PATHS"]["VOLUME_PATH_MAC"]+self.algo_name_selected+'/input_data'
        print("The log directory",self.input_file_path)
        #files_input_path = os.listdir(input_path)
        logfile_path = self.input_file_path
        print("log file path:",logfile_path)
        shutil.copy(logfile_path,self.algo_input_path)
        
        
        dock_manager = DockerManager()
       
        dock_manager.run_algorithm(self.algo_name_selected , self.log_name_selected, logfile_path)

        # adding o/p files to import log screen
        
        self.output_path = config["PATHS"]["VOLUME_PATH_MAC"]+self.algo_name_selected+'/output_data/'
        self.path = config["PATHS"]["VOLUME_PATH_MAC"]+'input_files/'
        
        files_output_path = os.listdir(self.output_path)
        

        print("output_path",self.output_path)
        print("input path",self.path)
        for file in files_output_path:
            print("o/p files",file)
            shutil.copy(self.output_path+file,self.path)
            if not file.startswith('.'):
                self.listImportedLog.addItem(file)
        self.buttonDisplay.setEnabled(True)
        self.buttonExport.setEnabled(True)

  
app= QtWidgets.QApplication(sys.argv)
MainWindow= QtWidgets.QMainWindow()
ui=FirstApp(MainWindow)
MainWindow.show()
app.exec_()