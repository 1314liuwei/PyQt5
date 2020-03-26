# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/14 10:13:37
@QQ :1044945158
@Version : 3.7
'''

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget

from widget import Ui_Widget


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)   
        self._ui = Ui_Widget()
        self._ui.setupUi(self)

    def on_pushButton_Total_clicked(self):  # 输出总价
        num = int(self._ui.lineEdit_Count.text())  # 获取数量
        price = float(self._ui.lineEdit_Price.text())  # 获取价格
        total = num * price
        self._ui.lineEdit_Total_Line.setText('%.2f'%total)  # 输出总价

    @pyqtSlot(int)
    def on_spinBox_valueChanged(self, weight: int):
        price = self._ui.doubleSpinBox.value()  # 获取价格
        self._ui.lineEdit_Total_Spin.setText(str(price * weight))  # 输出总价

    @pyqtSlot(float)
    def on_doubleSpinBox_valueChanged(self, price):
        widget = self._ui.spinBox.value()  # 获取重量
        self._ui.lineEdit_Total_Spin.setText(str(price * widget))  # 输出价格

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
