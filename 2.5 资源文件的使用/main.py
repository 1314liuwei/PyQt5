# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/13 11:55:52
@QQ :1044945158
@Version : 3.7
'''

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from human import Human
from widget import Ui_Widget


class QmyWideget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._ui = Ui_Widget()
        self._ui.setupUi(self)  # 创建UI

        self.human = Human(18, '小明')  # 绑定自定义信号
        self.human.nameChanged.connect(self.my_nameChanged)
        self.human.ageChanged[int].connect(self.my_ageChanged_int)
        self.human.ageChanged[str].connect(self.my_ageChanged_str)

    # ============自定义槽函数============
    def my_nameChanged(self, name):  # nameChanged(str)响应
        self._ui.lineEdit_nameStr.setText('Hello, %s!'%name)

    @pyqtSlot(int)
    def my_ageChanged_int(self, age):  # ageChanged(int)响应
        self._ui.lineEdit_ageInt.setText(str(age))
    
    @pyqtSlot(str)
    def my_ageChanged_str(self, info):  # ageChanged(str)响应
        self._ui.lineEdit_ageStr.setText(info)

    # ============自动关联槽函数============
    def on_slider_SetAge_valueChanged(self, value):  # 滑块改变年龄
        self.human.setAge(value)

    def on_pushButton_clicked(self):  # 设置姓名
        name = self._ui.lineEdit_inputName.text()
        self.human.setName(name)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    icon = QIcon(':/icons/images/app.ico')  # 设置应用程序图标
    app.setWindowIcon(icon)
    
    form = QmyWideget()
    form.show()
    sys.exit(app.exec_())
