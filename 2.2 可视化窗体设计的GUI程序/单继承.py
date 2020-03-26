# -*- encoding: utf-8 -*-
'''
@文件 : 单继承.py
@Time : 2020/03/12 12:17:25
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from FormHello import Ui_FormLabel

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)    # 创建窗口
        self._ui = Ui_FormLabel()    # UI对象
        self._ui.setupUi(self)    # 构造UI
        self.Lab = '单继承'
        self._ui.label.setText(self.Lab)

    def setBtnText(self, text):
        self._ui.pushButton.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.setBtnText('间接修改')
    sys.exit(app.exec_())

