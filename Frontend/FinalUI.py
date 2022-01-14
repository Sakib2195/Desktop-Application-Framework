from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        width = 800
        MainWindow.setFixedWidth(width)
        height = 680
        MainWindow.setFixedHeight(height)
        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1.setScaledContents(True)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet('color : #2B5DD1')
        self.label1.setObjectName("label1")
        self.label1.setGeometry(220,40,531,71)
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(70, 130, 661, 411))
        self.tabWidget.setObjectName("tabWidget")
        
       
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.buttonImportlog = QtWidgets.QPushButton(self.tab)
        self.buttonImportlog.setGeometry(QtCore.QRect(30, 30, 171, 31))
        self.buttonImportlog.setObjectName("buttonImportlog")
        self.listImportedLog = QtWidgets.QListWidget(self.tab)
        self.listImportedLog.setGeometry(QtCore.QRect(30, 81, 450, 181))
        self.listImportedLog.setObjectName("listImportedLog")
        self.buttonSelectDocker = QtWidgets.QPushButton(self.tab)
        self.buttonSelectDocker.setGeometry(QtCore.QRect(30, 290, 150, 41))
        self.buttonSelectDocker.setObjectName("buttonSelectDocker")

        

        self.buttonExport = QtWidgets.QPushButton(self.tab)
        self.buttonExport.setGeometry(QtCore.QRect(500, 330, 150, 41))
        self.buttonExport.setObjectName("buttonExport")

        # display button
        self.buttonDisplay = QtWidgets.QPushButton(self.tab)
        self.buttonDisplay.setGeometry(QtCore.QRect(500, 290, 150, 41))
        self.buttonDisplay.setObjectName("buttonDisplay")

        self.labelLogSummary = QtWidgets.QLabel(self.tab)
        self.labelLogSummary.setGeometry(QtCore.QRect(300, 60, 231, 280))
        self.labelLogSummary.setText("")
        self.labelLogSummary.setObjectName("labelLogSummary")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listAlgorithm = QtWidgets.QListWidget(self.tab_2)
        self.listAlgorithm.setGeometry(QtCore.QRect(10, 20, 256, 280))
        self.listAlgorithm.setObjectName("listAlgorithm")
    
        self.label_showAlgoSummary = QtWidgets.QTextEdit(self.tab_2)
        self.label_showAlgoSummary.setGeometry(QtCore.QRect(266, 20, 368, 280))
        self.label_showAlgoSummary.setObjectName("label_showAlgoSummary")
        self.buttonApplyAlgorithm = QtWidgets.QPushButton(self.tab_2)
        self.buttonApplyAlgorithm.setGeometry(QtCore.QRect(50, 300, 221, 51))
        self.buttonApplyAlgorithm.setObjectName("buttonApplyAlgorithm")

       
        
        self.tabWidget.addTab(self.tab_2, "")
        
        self.buttonExit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExit.setGeometry(QtCore.QRect(560, 570, 140, 35))
        self.buttonExit.setObjectName("buttonExit")
        self.buttonExit.setStyleSheet('QPushButton {background-color: #A3C1DA ; color: black;}')


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar") 
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Application Framework"))
        self.label1.setText(_translate("MainWindow", "Desktop Application Framework"))
        self.buttonExit.setText(_translate("MainWindow", "Quit Application"))
        self.buttonImportlog.setText(_translate("MainWindow", "Import Event Log"))
        self.buttonSelectDocker.setText(_translate("MainWindow", "Select Docker File"))
        self.buttonDisplay.setText(_translate("MainWindow", "Visualize"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Selection of Event Log"))
        self.buttonApplyAlgorithm.setText(_translate("MainWindow", "Apply the selected Algorithm"))
        self.buttonExport.setText(_translate("MainWindow", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Select Algorithm"))
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
