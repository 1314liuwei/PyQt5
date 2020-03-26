# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/19 15:44:22
@QQ :1044945158
@Version : 3.7
'''

import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import (
    QApplication, QListWidgetItem, QMainWindow, QMenu, QToolButton)

from mainWindow import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.setCentralWidget(self._ui.splitter)
        self.__setActionForButton()
        self.__createSelection()
        self.__Flageditable = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | \
            Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.__FlagNotEditable = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        | Qt.ItemIsEnabled)

    def __setActionForButton(self):  # 为 ToolButton 按钮设置 Action
        self._ui.toolButton.setDefaultAction(self._ui.action_InitList)
        self._ui.toolButton_2.setDefaultAction(self._ui.action_ClearList)
        self._ui.toolButton_3.setDefaultAction(self._ui.action_Insert)
        self._ui.toolButton_4.setDefaultAction(self._ui.action_DeleteItem)
        self._ui.toolButton_5.setDefaultAction(self._ui.action_InitList)

        # self._ui.toolButton_6.setDefaultAction(self._ui.action_Add)
        self._ui.toolButton_7.setDefaultAction(self._ui.action_ClearList)
        self._ui.toolButton_8.setDefaultAction(self._ui.action_DeleteItem)

    def __createSelection(self):  # 创建 ToolButton 按钮的下拉菜单
        menuselection = QMenu(self)
        menuselection.addAction(self._ui.action_Add)
        menuselection.addAction(self._ui.action_ClearList)
        menuselection.addAction(self._ui.action_DeleteItem)

        # ListWidget 上方的 btnSelectItem 按钮
        self._ui.toolButton_6.setPopupMode(QToolButton.MenuButtonPopup)
        self._ui.toolButton_6.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self._ui.toolButton_6.setDefaultAction(self._ui.action_Add)
        self._ui.toolButton_6.setMenu(menuselection)

        toolBtn = QToolButton(self)
        toolBtn.setPopupMode(QToolButton.InstantPopup)
        toolBtn.setDefaultAction(self._ui.action_ClearList)
        toolBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBtn.setMenu(menuselection)
        self._ui.toolBar.addWidget(toolBtn)

        self._ui.toolBar.addSeparator()
        self._ui.toolBar.addAction(self._ui.action_Add)
        
    def on_action_Add_triggered(self):  # 初始化列表
        icon = QIcon(':/icon/images/724.bmp')
        editable = self._ui.checkBox.isChecked()

        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        self._ui.listWidget.clear()
        for i in range(10):
            itemStr = 'Item %d'%i
            aItem = QListWidgetItem()
            aItem.setText(itemStr)
            aItem.setIcon(icon)
            aItem.setCheckState(Qt.Checked)
            aItem.setFlags(Flag)
            self._ui.listWidget.addItem(aItem)

    def on_action_Insert_triggered(self):
        icon = QIcon(':/icon/images/724.bmp')
        editable = self._ui.checkBox.isChecked()

        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        aItem = QListWidgetItem()
        aItem.setText('Insert Item')
        aItem.setIcon(icon)
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)
        curRow = self._ui.listWidget.currentRow()
        self._ui.listWidget.insertItem(curRow, aItem)
        
    def on_action_Delete_triggered(self):
        row = self._ui.listWidget.currentRow()
        self._ui.listWidget.takeItem(row)

    def on_action_Clear_triggered(self):
        self._ui.listWidget.clear()

    def on_action_All_triggered(self):
        for i in range(self._ui.listWidget.count()):
            aItem = self._ui.listWidget.item(i)
            aItem.setCheckState(Qt.checked)

    def on_action_None_triggered(self):
        for i in range(self._ui.listWidget.count()):
            aItem = self._ui.listWidget.item(i)
            aItem.setCheckState(Qt.Unchecked)

    def on_action_Invs_triggered(self):
        for i in range(self._ui.listWidget.count()):
            aItem = self._ui.listWidget.item(i)
            if aItem.checkState() != Qt.Checked:
                aItem.setCheckState(Qt.checked)
            else:
                aItem.setCheckState(Qt.Unchecked)

    def on_listWidget_currentItemChanged(self, current, previous):
        strInfo = ''
        if current:
            if previous:
                strInfo = f'当前：{current.text()};前一项：{previous.text()}'
            else:
                strInfo = f'当前：{current.text()}'
        self._ui.lineEdit.setText(strInfo)

    def on_listWidget_customContextMenuRequested(self, pos):
        menuList = QMenu(self)
        menuList.addAction(self._ui.action_InitList)
        menuList.addAction(self._ui.action_Add)
        menuList.addAction(self._ui.action_ClearList)
        menuList.addAction(self._ui.action_Insert)
        menuList.addAction(self._ui.action_DeleteItem)
        menuList.exec(QCursor.pos())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
