# -*- encoding: utf-8 -*-
'''
@文件 : myDialog.py
@Time : 2020/03/12 18:11:55
@QQ :1044945158
@Version : 3.7
'''

import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPalette, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QDialog

from dialog import Ui_Dialog


class QmyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)  # 构造窗体
        self._ui = Ui_Dialog()  # 构造UI对象
        self._ui.setupUi(self)  # 构造UI

        # 将信号与函数绑定
        self._ui.radioRed.clicked.connect(self.my_setTextColor)
        self._ui.radioBlack.clicked.connect(self.my_setTextColor)
        self._ui.radioBlue.clicked.connect(self.my_setTextColor)

    def on_btnClear_clicked(self):  # 清除文本框
        self._ui.textEdit.clear()

    @pyqtSlot(bool)
    def on_checkBoxBold_clicked(self, checked: bool):  # 设置粗体
        font = self._ui.textEdit.font()  # 获取字体样式
        font.setBold(checked)  # 设置粗体
        self._ui.textEdit.setFont(font)  # 改变文本框字体c

    # @pyqtSlot(bool)
    def on_chkBoxUnder_clicked(self):  # 设置下划线
        font = self._ui.textEdit.font()
        checked = self._ui.chkBoxUnder.isChecked()  # 获取勾选状态,和使用装饰器效果一致
        font.setUnderline(checked)
        self._ui.textEdit.setFont(font)
        

    @pyqtSlot(bool)
    def on_chkBoxItalic_clicked(self, checked: bool):  # 示威者斜体
        font = self._ui.textEdit.font()
        font.setItalic(checked)
        self._ui.textEdit.setFont(font)

    def my_setTextColor(self):  # 设置颜色
        palette = self._ui.textEdit.palette()  # 获取字体调色板

        if (self._ui.radioBlack.isChecked()):  # 更改调色板颜色
            palette.setColor(QPalette.Text, Qt.black)
        elif (self._ui.radioBlue.isChecked()):
            palette.setColor(QPalette.Text, Qt.blue)
        else:
            palette.setColor(QPalette.Text, Qt.red)

        self._ui.textEdit.setPalette(palette)  # 设置字体颜色


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyDialog()
    form.show()
    sys.exit(app.exec_())
