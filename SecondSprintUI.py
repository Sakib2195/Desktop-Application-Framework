from os import path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout
#from firstSprintUI import*
from FinalUI import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from window3 import Ui_window2
import pandas as pd
from pm4py.objects.log.importer.xes import importer as xes_importer
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex
import docker
import time

class FirstApp(Ui_MainWindow):

    def __init__(self,window):
        self.setupUi(window)
        self.direcname= " "
        self.button_importLog.clicked.connect(self.logload)
        self.button_showLogSummary.clicked.connect(self.showLogSummary)
        self.button_selectAlgo.clicked.connect(self.goTab)
        self.button_applyAlgo.clicked.connect(self.openWindow)
        #self.button_applyAlgo.clicked.connect(self.showAlgorithms)
    def logload(self):
        filename=QFileDialog.getOpenFileName()
        self.direcname = filename[0]
        self.log_name = QFileInfo(self.direcname).fileName()
        self.list_importedLog.addItem(self.log_name)
        print(self.log_name)
    def showLogSummary(self):
        log = xes_importer.apply(self.direcname)
        print(log[0])
        self.label_showSummary.setText(str(log[0]))
        #self.label_showSummary.setWordWrap(True)
    def goTab(self):
        self.App_Tab.setCurrentIndex(1)
    def openWindow(self):
        client = docker.from_env()
        volumes= ['/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/alpha_miner']
        volume_bindings = {
                            '/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/alpha_miner': {
                                'bind': '/alpha_miner',
                                'mode': 'rw',
                            },
        }

        host_config = client.api.create_host_config(
                            binds=volume_bindings
        )

        container = client.api.create_container(
                            image='am',
                            name="alpha_miner_container",
                            volumes=volumes,
                            host_config=host_config,
                            command='running-example.xes'
        ) 
        response = client.api.start(container=container.get('Id'))

        time.sleep(5)

        



  
app= QtWidgets.QApplication(sys.argv)
MainWindow= QtWidgets.QMainWindow()
ui=FirstApp(MainWindow)
MainWindow.show()
app.exec_()


