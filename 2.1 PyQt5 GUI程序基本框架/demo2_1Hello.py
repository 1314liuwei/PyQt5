# -*- encoding: utf-8 -*-
'''
@文件 : demo2_1Hello.py
@Time : 2020/03/11 22:38:04
@QQ :1044945158
@Version : 3.7
'''

import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)    # 创建app, 用QApplication类
widgetHello = QtWidgets.QWidget()         # 创建窗体, 用QWidget类
widgetHello.resize(500, 150)              # 设置窗体的宽度和高度
widgetHello.setWindowTitle('Demo2_1')     # 设置窗体的标题文字

LabHello = QtWidgets.QLabel(widgetHello)  # 创建标签, 父容器为widgetHello
LabHello.setText('Hello World, PyQt5!')   # 设置标签文字

font = QtGui.QFont()          # 使用QFont类创建字体对象font
font.setPointSize(12)         # 设置字体大小
font.setBold(True)            # 设置为粗体

LabHello.setFont(font)        # 设置为标签LabHello的字体
size = LabHello.sizeHint()    # 获取LabHello的合适大小, 得到一个size对象
LabHello.setGeometry(70, 60, size.width(), size.height())

widgetHello.show()   # 显示对话框
sys.exit(app.exec_())  # 运行程序

