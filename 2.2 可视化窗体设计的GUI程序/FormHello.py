# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Study\2.2.1\FormHello.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormLabel(object):
    def setupUi(self, FormLabel):
        FormLabel.setObjectName("FormLabel")
        FormLabel.resize(767, 538)
        self.label = QtWidgets.QLabel(FormLabel)
        self.label.setGeometry(QtCore.QRect(80, 120, 731, 211))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FormLabel)
        self.pushButton.setGeometry(QtCore.QRect(320, 430, 112, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(FormLabel)
        QtCore.QMetaObject.connectSlotsByName(FormLabel)

    def retranslateUi(self, FormLabel):
        _translate = QtCore.QCoreApplication.translate
        FormLabel.setWindowTitle(_translate("FormLabel", "Form"))
        self.label.setText(_translate("FormLabel", "Hello World, PyQt5!"))
        self.pushButton.setText(_translate("FormLabel", "关闭"))
