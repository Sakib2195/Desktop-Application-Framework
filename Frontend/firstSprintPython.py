from os import path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout
from firstSprintUI import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import pandas as pd
from pm4py.objects.log.importer.xes import importer as xes_importer

class FirstApp(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.direcname= " "
        self.button_importLog.clicked.connect(self.logload)
        self.button_showLogSummary.clicked.connect(self.showLogSummary)
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
        self.label_showSummary.setWordWrap(True)

  
app= QtWidgets.QApplication(sys.argv)
MainWindow= QtWidgets.QMainWindow()
ui=FirstApp(MainWindow)
MainWindow.show()
app.exec_()