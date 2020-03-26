# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/21 15:43:50
@QQ :1044945158
@Version : 3.7
'''

import sys
from enum import Enum

from PyQt5.QtCore import QDir, QFileInfo, Qt, pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QDockWidget, QFileDialog, QLabel,
                             QMainWindow, QTreeWidget, QTreeWidgetItem)

from mainwindow import Ui_MainWindow


class TreeItemType(Enum):
    ItTopItem = 1001
    ItGroupItem = 1002
    ItImageItem = 1003


class TreeColNum(Enum):
    ColItem = 0
    ColItemType = 1


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.curPixmap = QPixmap()
        self.pixRatio = 1
        self.itemFlags = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        | Qt.ItemIsEnabled | Qt.ItemIsAutoTristate)

        self.setCentralWidget(self._ui.scrollArea)
        self.__iniTree()

    def __iniTree(self):
        self._ui.treeWidget.clear()
        icon = QIcon(':/icons/icons/15.ico')

        item = QTreeWidgetItem(TreeItemType.ItTopItem.value)
        item.setIcon(TreeColNum.ColItem.value, icon)
        item.setText(TreeColNum.ColItem.value, '图片文件')
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.ColItem.value, Qt.Checked)
        item.setData(TreeColNum.ColItem.value, Qt.UserRole, '')
        self._ui.treeWidget.addTopLevelItem(item)

    def on_action_OpenFolder_triggered(self):
        dirStr = QFileDialog.getExistingDirectory()
        if not dirStr:
            return

        parItem = self._ui.treeWidget.currentItem()
        if not parItem:
            parItem = self._ui.treeWidget.topLevelItem(0)

        icon = QIcon(':/icons/icons/open3.bmp')
        dirObj = QDir(dirStr)
        nodeText = dirObj.dirName()

        item = QTreeWidgetItem(TreeItemType.ItGroupItem.value)
        item.setIcon(TreeColNum.ColItem.value, icon)
        item.setText(TreeColNum.ColItem.value, nodeText)
        item.setText(TreeColNum.ColItemType.value, 'Group')
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.ColItem.value, Qt.Checked)
        item.setData(TreeColNum.ColItem.value, Qt.UserRole, dirStr)
        parItem.addChild(item)
        parItem.setExpanded(True)

    def on_action_OpenFile_triggered(self):
        fileList, flt = QFileDialog.getOpenFileNames(self, '选择一个或多个文件', '', 'Images(*.jpg)')
        if len(fileList) < 1:
            return
        
        item = self._ui.treeWidget.currentItem()
        if item.type() == TreeItemType.ItImageItem.value:
            parItem = item.parent()
        else:
            parItem = item

        icon = QIcon(':/icons/icons/31.ico')
        for fullFileName in fileList:
            fileinfo = QFileInfo(fullFileName)
            nodeText = fileinfo.fileName()

            item = QTreeWidgetItem(TreeColNum.ColItem.value)
            item.setIcon(TreeColNum.ColItem.value, icon)
            item.setText(TreeColNum.ColItem.value, nodeText)
            item.setText(TreeColNum.ColItemType.value, 'Image')
            item.setFlags(self.itemFlags)
            item.setCheckState(TreeColNum.ColItem.value, Qt.Checked)
            item.setData(TreeColNum.ColItem.value, Qt.UserRole, fullFileName)
            parItem.addChild(item)

        parItem.setExpanded(True)

    def on_treeWidget_currentItemChanged(self, current, previous):
        if not current:
            return

        nodeType = current.type()
        if nodeType == TreeItemType.ItTopItem.value:
            self._ui.action_OpenFolder.setEnabled(True)
            self._ui.action_OpenFile.setEnabled(True)
            self._ui.action_Delete.setEnabled(False)
        elif nodeType == TreeItemType.ItGroupItem.value:
            self._ui.action_OpenFolder.setEnabled(True)
            self._ui.action_OpenFile.setEnabled(True)
            self._ui.action_Delete.setEnabled(True)
        else:
            self._ui.action_OpenFolder.setEnabled(False)
            self._ui.action_OpenFile.setEnabled(True)
            self._ui.action_Delete.setEnabled(False)
            self.__displayImage(current)

    def on_action_Delete_triggered(self):
        item = self._ui.treeWidget.currentItem()
        parItem = item.parent()
        parItem.removeChild(item)

    def on_action_Ergodic_triggered(self):
        count = self._ui.treeWidget.topLevelItemCount()
        for i in range(count):
            item = self._ui.treeWidget.topLevelItem(i)
            self.__changedItemCaption(item)

    def __changedItemCaption(self, item):
        title = f'*{item.text(TreeColNum.ColItem.value)}'
        item.setText(TreeColNum.ColItem.value, title)
        if item.childCount() > 0:
            for i in range(item.childCount()):
                self.__changedItemCaption(item.child(i))

    def __displayImage(self, item):
        filename = item.data(TreeColNum.ColItem.value, Qt.UserRole)
        self._ui.statusBar.showMessage(filename)
        self.curPixmap.load(filename)
        self.on_action_SuitableHeight_triggered()
        self._ui.action_SuitableHeight.setEnabled(True)
        self._ui.action_SuitableWidth.setEnabled(True)
        self._ui.action_Narrow.setEnabled(True)
        self._ui.action_Enlarge.setEnabled(True)
        self._ui.action_Actual.setEnabled(True)

    def on_action_SuitableHeight_triggered(self):
        H = self._ui.scrollArea.height()
        realH = self.curPixmap.height()
        self.pixRation = float(H) / realH
        pix = self.curPixmap.scaledToHeight(H - 30)
        self._ui.label.setPixmap(pix)

    def on_action_SuitableWidth_triggered(self):
        W = self._ui.scrollArea.width()
        realW = self.curPixmap.width()
        self.pixRation = float(W) / realW
        pix = self.curPixmap.scaledToWidth(W - 30)
        self._ui.label.setPixmap(pix)

    def on_action_Enlarge_triggered(self):
        self.pixRatio = self.pixRatio * 1.2
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self._ui.label.setPixmap(pix)

    def on_action_Narrow_triggered(self):
        self.pixRatio = self.pixRatio * 0.8
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self._ui.label.setPixmap(pix)

    def on_action_Actual_triggered(self):
        self.pixRatio = 1
        self._ui.label.setPixmap(self.curPixmap)

    # def on

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
