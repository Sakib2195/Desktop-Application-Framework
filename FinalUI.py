# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(130, 40, 531, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_heading.setScaledContents(True)
        self.label_heading.setWordWrap(True)
        self.label_heading.setObjectName("label_heading")
        self.App_Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.App_Tab.setGeometry(QtCore.QRect(20, 100, 661, 411))
        self.App_Tab.setObjectName("App_Tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.button_importLog = QtWidgets.QPushButton(self.tab)
        self.button_importLog.setGeometry(QtCore.QRect(30, 40, 171, 31))
        self.button_importLog.setObjectName("button_importLog")
        self.list_importedLog = QtWidgets.QListWidget(self.tab)
        self.list_importedLog.setGeometry(QtCore.QRect(30, 120, 291, 181))
        self.list_importedLog.setObjectName("list_importedLog")
        self.button_selectAlgo = QtWidgets.QPushButton(self.tab)
        self.button_selectAlgo.setGeometry(QtCore.QRect(30, 320, 251, 41))
        self.button_selectAlgo.setObjectName("button_selectAlgo")
        self.label_importLog = QtWidgets.QLabel(self.tab)
        self.label_importLog.setGeometry(QtCore.QRect(30, 20, 231, 16))
        self.label_importLog.setObjectName("label_importLog")
        self.button_showLogSummary = QtWidgets.QPushButton(self.tab)
        self.button_showLogSummary.setGeometry(QtCore.QRect(450, 290, 191, 32))
        self.button_showLogSummary.setObjectName("button_showLogSummary")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_showSummary = QtWidgets.QTextEdit(self.tab)
        self.label_showSummary.setGeometry(QtCore.QRect(390, 70, 251, 221))
        self.label_showSummary.setObjectName("label_showSummary")
        self.App_Tab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.List_Algorithms = QtWidgets.QListWidget(self.tab_2)
        self.List_Algorithms.setGeometry(QtCore.QRect(10, 50, 291, 321))
        self.List_Algorithms.setObjectName("List_Algorithms")
        item = QtWidgets.QListWidgetItem()
        self.List_Algorithms.addItem(item)
        self.button_applyAlgo = QtWidgets.QPushButton(self.tab_2)
        self.button_applyAlgo.setGeometry(QtCore.QRect(380, 170, 221, 51))
        self.button_applyAlgo.setObjectName("button_applyAlgo")
        self.label_selectAlgorithm = QtWidgets.QLabel(self.tab_2)
        self.label_selectAlgorithm.setGeometry(QtCore.QRect(10, 20, 171, 16))
        self.label_selectAlgorithm.setObjectName("label_selectAlgorithm")
        self.App_Tab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 320, 171, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.App_Tab.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.App_Tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "Desktop Application Framework"))
        self.button_importLog.setText(_translate("MainWindow", "Import Log from PC"))
        self.button_selectAlgo.setText(_translate("MainWindow", "Select Docker File"))
        self.label_importLog.setText(_translate("MainWindow", "Import an event log to get started"))
        self.button_showLogSummary.setText(_translate("MainWindow", "Show log summary"))
        self.label_3.setText(_translate("MainWindow", "Imported Log"))
        self.App_Tab.setTabText(self.App_Tab.indexOf(self.tab), _translate("MainWindow", "Log Selection"))
        __sortingEnabled = self.List_Algorithms.isSortingEnabled()
        self.List_Algorithms.setSortingEnabled(False)
        item = self.List_Algorithms.item(0)
        item.setText(_translate("MainWindow", "Alpha Miner Algorithm"))
        self.List_Algorithms.setSortingEnabled(__sortingEnabled)
        self.button_applyAlgo.setText(_translate("MainWindow", "Apply the selected Algorithm"))
        self.label_selectAlgorithm.setText(_translate("MainWindow", "Select an algorithm"))
        self.App_Tab.setTabText(self.App_Tab.indexOf(self.tab_2), _translate("MainWindow", "Algorithm"))
        self.pushButton_4.setText(_translate("MainWindow", "Export"))
        self.App_Tab.setTabText(self.App_Tab.indexOf(self.tab_3), _translate("MainWindow", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

