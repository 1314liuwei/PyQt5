# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Study\3.5 定时器QTimer\QtApp\widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(592, 388)
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 551, 141))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 531, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Start.setAutoExclusive(False)
        self.pushButton_Start.setFlat(False)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.gridLayout.addWidget(self.pushButton_Start, 0, 0, 1, 1)
        self.pushButton_SetTime = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_SetTime.setObjectName("pushButton_SetTime")
        self.gridLayout.addWidget(self.pushButton_SetTime, 1, 0, 1, 1)
        self.pushButton_Stop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Stop.setAutoExclusive(False)
        self.pushButton_Stop.setFlat(False)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.gridLayout.addWidget(self.pushButton_Stop, 0, 1, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 170, 551, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 531, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber_Hour = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_Hour.setObjectName("lcdNumber_Hour")
        self.horizontalLayout.addWidget(self.lcdNumber_Hour)
        self.lcdNumber_Minute = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_Minute.setObjectName("lcdNumber_Minute")
        self.horizontalLayout.addWidget(self.lcdNumber_Minute)
        self.lcdNumber_Second = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_Second.setObjectName("lcdNumber_Second")
        self.horizontalLayout.addWidget(self.lcdNumber_Second)
        self.label_Reduce = QtWidgets.QLabel(Widget)
        self.label_Reduce.setGeometry(QtCore.QRect(20, 347, 281, 31))
        self.label_Reduce.setObjectName("label_Reduce")
        self.pushButton_4 = QtWidgets.QPushButton(Widget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 350, 112, 34))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Widget)
        self.pushButton_4.clicked.connect(Widget.close)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.groupBox.setTitle(_translate("Widget", "定时器"))
        self.pushButton_Start.setText(_translate("Widget", "开始"))
        self.pushButton_SetTime.setText(_translate("Widget", "设置时间"))
        self.pushButton_Stop.setText(_translate("Widget", "停止"))
        self.groupBox_2.setTitle(_translate("Widget", "当前时间（时：分：秒）"))
        self.label_Reduce.setText(_translate("Widget", "时间已过去："))
        self.pushButton_4.setText(_translate("Widget", "关闭"))
