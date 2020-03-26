# -*- encoding: utf-8 -*-
'''
@文件 : appMain1.py
@Time : 2020/03/12 10:40:44
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5 import QtWidgets
import FormHello

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    baseWidget = QtWidgets.QWidget()    # 创建窗体的基类QWidget的实例

    ui = FormHello.Ui_FormLabel()
    ui.setupUi(baseWidget)    # 将baseWidget传递给setipUi方法创建完整窗体

    baseWidget.show()
    sys.exit(app.exec_())