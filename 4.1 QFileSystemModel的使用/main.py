# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/26 19:12:52
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel
from PyQt5.QtCore import QDir
from mainwindow import Ui_MainWindow

class QmyMaindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.__Build()

    def __Build(self):
        self.model = QFileSystemModel(self)
        print(QDir.currentPath())
        self.model.setRootPath('')
        self._ui.treeView.setModel(self.model)
        self._ui.listView.setModel(self.model)
        self._ui.tableView.setModel(self.model)
        self._ui.treeView.clicked.connect(self._ui.listView.setRootIndex)
        self._ui.treeView.clicked.connect(self._ui.tableView.setRootIndex)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyMaindow()
    form.show()
    sys.exit(app.exec_())