# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/17 15:22:10
@QQ :1044945158
@Version : 3.7
'''

import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QFont, QTextCharFormat
from PyQt5.QtWidgets import (
    QActionGroup, QApplication, QFontComboBox, QLabel, QMainWindow,
    QProgressBar, QSpinBox)

from mainWindow import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._buildUi()  # 动态创建组件，添加到工具栏和状态栏
        self._spinFontSize.valueChanged[int].connect(self.my_fontSize_Changed)  # 字体大小设置
        self._comboFontName.currentIndexChanged[str].connect(self.my_fontName_Changed)  #字体选择
        self.setCentralWidget(self._ui.plainTextEdit)  # 将文本框防止中央

    def _buildUi(self):
        # QLable显示信息
        self._LabFile = QLabel(self)
        self._LabFile.setMinimumWidth(150)
        self._LabFile.setText('文件名：')
        self._ui.statusBar.addWidget(self._LabFile)  # 添加到状态栏

        # progressBar显示
        self._progressBar1 = QProgressBar(self)
        self._progressBar1.setMaximumWidth(200)
        self._progressBar1.setMinimum(5)
        self._progressBar1.setMaximum(50)
        sz = self._ui.plainTextEdit.font().pointSize()
        self._progressBar1.setValue(sz)  # 将字体大小显示在progressBar
        self._ui.statusBar.addWidget(self._progressBar1)  # 添加到状态栏

        self._LabInfo = QLabel(self)
        self._LabInfo.setText('选择字体名称：{黑体}')
        self._ui.statusBar.addPermanentWidget(self._LabInfo)

        actionGroup = QActionGroup(self)
        actionGroup.addAction(self._ui.action_English)
        actionGroup.addAction(self._ui.action_Chinese)
        actionGroup.setExclusive(True)
        self._ui.action_Chinese.setChecked(True)

        self._spinFontSize = QSpinBox(self)
        self._spinFontSize.setMinimum(5)
        self._spinFontSize.setMaximum(50)
        sz = self._ui.plainTextEdit.font().pointSize()
        self._spinFontSize.setValue(sz)
        self._spinFontSize.setMinimumWidth(50)
        self._ui.toolBar.addWidget(self._spinFontSize)

        self._comboFontName = QFontComboBox(self)
        self._comboFontName.setMinimumWidth(100)
        self._ui.toolBar.addWidget(self._comboFontName)

        self._ui.toolBar.addSeparator()
        self._ui.toolBar.addAction(self._ui.action_Close)

    @pyqtSlot(int)
    def my_fontSize_Changed(self, fontsize):
        fmt = self._ui.plainTextEdit.currentCharFormat()
        fmt.setFontPointSize(fontsize)
        self._ui.plainTextEdit.mergeCurrentCharFormat(fmt)
        self._progressBar1.setValue(fontsize)

    @pyqtSlot(str)
    def my_fontName_Changed(self, fontName):
        fmt = self._ui.plainTextEdit.currentCharFormat()
        fmt.setFontFamily(fontName)
        self._ui.plainTextEdit.mergeCurrentCharFormat(fmt)
        self._LabInfo.setText(f'字体名称：{fontName}')

    @pyqtSlot(bool)
    def on_action_Bold_triggered(self, checked):
        fmt = self._ui.plainTextEdit.currentCharFormat()
        if checked:
            fmt.setFontWeight(QFont.Bold)
        else:
            fmt.setFontWeight(QFont.Normal)
        self._ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def on_action_Italic_triggered(self, checked):
        fmt = self._ui.plainTextEdit.currentCharFormat()
        fmt.setFontItalic(checked)
        self._ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def on_action_UnderLine_triggered(self, checked):
        fmt = self._ui.plainTextEdit.currentCharFormat()
        fmt.setFontUnderline(checked)
        self._ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    def on_plainTextEdit_copyAvailable(self, avi):
        self._ui.action_Copy.setEnabled(avi)
        self._ui.action_Cut.setEnabled(avi)
        self._ui.action_Paste.setEnabled(self._ui.plainTextEdit.canPaste())

    def on_plainTextEdit_selectionChanged(self):
        fmt = self._ui.plainTextEdit.currentCharFormat()
        self._ui.action_Bold.setChecked(fmt.font().bold())
        self._ui.action_Italic.setChecked(fmt.fontItalic())
        self._ui.action_UnderLine.setChecked(fmt.fontUnderline())
    
    def on_plainTextEdit_customeContexMenuRequested(self, pos):
        popMenu = self._ui.plainTextEdit.createStandardContextMenu()
        popMenu.exec(pos)

    @pyqtSlot(bool)
    def on_action_Text_triggered(self, checked):
        if checked:
            st = Qt.ToolButtonTextUnderIcon
        else:
            st = Qt.ToolButtonIconOnly
        self._ui.toolBar.setToolButtonStyle(st)

    def on_action_New_triggered(self):
        self._LabFile.setText('新建文件')

    def on_action_Open_triggered(self):
        self._LabFile.setText('打开文件')

    def on_action_Save_triggered(self):
        self._LabFile.setText('文件已保存')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
