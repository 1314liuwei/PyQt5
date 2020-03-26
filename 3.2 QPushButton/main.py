# -*- encoding: utf-8 -*-
'''
@文件 : man.py
@Time : 2020/03/14 15:19:41
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont
from widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self._ui = Ui_Widget()
        self._ui.setupUi(self)

    # ==== 自关联槽函数 ====
    def on_pushButton_Left_clicked(self):  # 居左
        self._ui.lineEdit.setAlignment(Qt.AlignLeft)

    def on_pushButton_Center_clicked(self):  # 居中
        self._ui.lineEdit.setAlignment(Qt.AlignCenter)

    def on_pushButton_Right_clicked(self):  # 居右
        self._ui.lineEdit.setAlignment(Qt.AlignRight)

    @pyqtSlot(bool)
    def on_pushButton_Bold_clicked(self, checked: bool):  # 加粗
        font = self._ui.lineEdit.font()
        font.setBold(checked)
        self._ui.lineEdit.setFont(font)

    @pyqtSlot(bool)
    def on_pushButton_Italic_clicked(self, checked: bool):  # 斜体
        font = self._ui.lineEdit.font()
        font.setItalic(checked)
        self._ui.lineEdit.setFont(font)

    @pyqtSlot(bool)
    def on_pushButton_Underline_clicked(self, checked: bool):  # 下划线
        font = self._ui.lineEdit.font()
        font.setUnderline(checked)
        self._ui.lineEdit.setFont(font)

    @pyqtSlot(bool)
    def on_checkBox_ReadOnly_clicked(self, checked: bool):  # ReadOnly
        self._ui.lineEdit.setReadOnly(checked)

    @pyqtSlot(bool)
    def on_checkBox_EnaBled_clicked(self, checked: bool):  # EnaBled
        self._ui.lineEdit.setEnabled(checked)

    @pyqtSlot(bool)
    def on_checkBox_ClearButtonEnabled_clicked(self, checked: bool):  # ClearButtonEnabled
        self._ui.lineEdit.setClearButtonEnabled(checked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())