# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/14 20:16:13
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot
from widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._ui = Ui_Widget()
        self._ui.setupUi(self)

        # 绑定信号
        self._ui.horizontalSlider.valueChanged.connect(self.my_valueChanged)
        self._ui.horizontalScrollBar.valueChanged.connect(self.my_valueChanged)

    @pyqtSlot(bool)
    def on_checkBox_Text_clicked(self, checked: bool):  # 设置TextVisible
        self._ui.progressBar.setTextVisible(checked)
    
    @pyqtSlot(bool)
    def on_checkBox_Inverted_clicked(self, checked: bool):  # 倒转
        self._ui.progressBar.setInvertedAppearance(checked)

    
    def on_radioButton_Percent_clicked(self):  # 设置显示格式
        self._ui.progressBar.setFormat('%p%')
    
    def on_radioButton_Value_clicked(self):  # 设置显示格式
        self._ui.progressBar.setFormat('%v')

    def my_valueChanged(self, value):  # 改变progressBar的值
        self._ui.progressBar.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())