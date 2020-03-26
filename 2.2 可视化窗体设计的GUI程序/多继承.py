# -*- encoding: utf-8 -*-
'''
@文件 : 多继承.py
@Time : 2020/03/12 11:54:03
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from FormHello import Ui_FormLabel

class QmyWidget(QWidget, Ui_FormLabel):
    def __init__(self, parent=None):
        super().__init__(parent)    # 调用QWidget类, 创建窗体

        self.Lab = '多继承'
        self.setupUi(self)    # 将窗体传递给setupUI
        self.label.setText(self.Lab)    # 设置label组件显示的文字


if __name__ == "__main__":
    app = QApplication(sys.argv)    # 创建app
    myWidget = QmyWidget()
    myWidget.show()    # 显示窗体
    myWidget.pushButton.setText('Close！')    # 更改pushButton组件显示的内容
    sys.exit(app.exec_())
