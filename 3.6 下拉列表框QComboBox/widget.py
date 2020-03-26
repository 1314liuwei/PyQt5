# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Study\3.6 下拉列表框QComboBox\QtApp\widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(661, 275)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        Widget.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 641, 80))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 621, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 301, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_InitList = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_InitList.setGeometry(QtCore.QRect(10, 30, 112, 34))
        self.pushButton_InitList.setObjectName("pushButton_InitList")
        self.pushButton_ClearList = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_ClearList.setGeometry(QtCore.QRect(180, 30, 112, 34))
        self.pushButton_ClearList.setObjectName("pushButton_ClearList")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 80, 105, 22))
        self.checkBox.setObjectName("checkBox")
        self.comboBox_City = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_City.setGeometry(QtCore.QRect(10, 120, 271, 24))
        self.comboBox_City.setObjectName("comboBox_City")
        self.comboBox_City.addItem("")
        self.comboBox_City.addItem("")
        self.comboBox_City.addItem("")
        self.comboBox_City.addItem("")
        self.comboBox_City.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(Widget)
        self.groupBox_3.setGeometry(QtCore.QRect(320, 90, 331, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 311, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_InitCity = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_InitCity.setObjectName("pushButton_InitCity")
        self.verticalLayout.addWidget(self.pushButton_InitCity)
        self.comboBox_User = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_User.setObjectName("comboBox_User")
        self.verticalLayout.addWidget(self.comboBox_User)
        self.pushButton_Close = QtWidgets.QPushButton(Widget)
        self.pushButton_Close.setGeometry(QtCore.QRect(530, 230, 112, 34))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Close.setIcon(icon)
        self.pushButton_Close.setObjectName("pushButton_Close")

        self.retranslateUi(Widget)
        self.pushButton_Close.clicked.connect(Widget.close)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.groupBox.setTitle(_translate("Widget", "选择内容"))
        self.groupBox_2.setTitle(_translate("Widget", "简单的ComboBox"))
        self.pushButton_InitList.setText(_translate("Widget", "初始化列表"))
        self.pushButton_ClearList.setText(_translate("Widget", "清除列表"))
        self.checkBox.setText(_translate("Widget", "可编辑"))
        self.comboBox_City.setItemText(0, _translate("Widget", "绵阳市"))
        self.comboBox_City.setItemText(1, _translate("Widget", "达州市"))
        self.comboBox_City.setItemText(2, _translate("Widget", "德阳市"))
        self.comboBox_City.setItemText(3, _translate("Widget", "资阳市"))
        self.comboBox_City.setItemText(4, _translate("Widget", "成都市"))
        self.groupBox_3.setTitle(_translate("Widget", "带有用户数据的ComboBox"))
        self.pushButton_InitCity.setText(_translate("Widget", "初始化城市"))
        self.pushButton_Close.setText(_translate("Widget", "关闭"))
import icons_rc
