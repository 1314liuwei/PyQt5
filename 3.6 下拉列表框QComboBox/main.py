# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/16 15:42:47
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

from widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._ui = Ui_Widget()
        self._ui.setupUi(self)

    def on_pushButton_InitList_clicked(self):
        icon = QIcon(':/new/prefix1/images/unit.ico')
        self._ui.comboBox_City.clear()
        city = ['绵阳市', '成都市', '德阳市', '资阳市', '达州市']
        for name in city:
            self._ui.comboBox_City.addItem(icon, name)

    def on_pushButton_ClearList_clicked(self):
        self._ui.comboBox_City.clear()

    def on_pushButton_InitCity_clicked(self):
        icon = QIcon(':/new/prefix1/images/aim.ico')
        self._ui.comboBox_User.clear()
        cities = {'Beijing':10, 'shanghai':21, 'tianjin':22}
        for k,v in cities.items():
            self._ui.comboBox_User.addItem(icon, k, v)
    
    @pyqtSlot(bool)
    def on_checkBox_clicked(self, checked):
        self._ui.comboBox_City.setEditable(checked)
    
    @pyqtSlot(str)
    def on_comboBox_City_currentIndexChanged(self, curText):
        self._ui.lineEdit.setText(curText)

    @pyqtSlot(str)
    def on_comboBox_User_currentIndexChanged(self, curText):
        self._ui.lineEdit.setText(curText)
        zone = self._ui.comboBox_User.currentData()
        if zone:
            self._ui.lineEdit.setText(f'城市：{curText}区号：{zone}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())