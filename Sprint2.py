# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sprint2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectAlgorithm(object):
    def setupUi(self, SelectAlgorithm):
        SelectAlgorithm.setObjectName("SelectAlgorithm")
        SelectAlgorithm.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(SelectAlgorithm)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(SelectAlgorithm)
        self.buttonBox.accepted.connect(SelectAlgorithm.accept)
        self.buttonBox.rejected.connect(SelectAlgorithm.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectAlgorithm)

    def retranslateUi(self, SelectAlgorithm):
        _translate = QtCore.QCoreApplication.translate
        SelectAlgorithm.setWindowTitle(_translate("SelectAlgorithm", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectAlgorithm = QtWidgets.QDialog()
    ui = Ui_SelectAlgorithm()
    ui.setupUi(SelectAlgorithm)
    SelectAlgorithm.show()
    sys.exit(app.exec_())

