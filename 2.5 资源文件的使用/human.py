# -*- encoding: utf-8 -*-
'''
@文件 : human.py
@Time : 2020/03/13 09:25:20
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Human(QObject):
    nameChanged = pyqtSignal(str)
    ageChanged = pyqtSignal([int], [str])

    def __init__(self, age, name, parent=None):
        super().__init__(parent=parent)
        self.setAge(age)
        self.setName(name)

    def setAge(self, age):
        self._age = age
        self.ageChanged[int].emit(self._age)
        if age <= 18:
            ageinfo = '骚年'
        elif 18 < age <= 35:
            ageinfo = '青年'
        elif 35 < age <= 55:
            ageinfo = '油腻中年'
        elif 55 < age <= 80:
            ageinfo = '老人'
        else:
            ageinfo = '老寿星'
        self.ageChanged[str].emit(ageinfo)

    def setName(self, name):
        self._name = name
        self.nameChanged.emit(self._name)

class Response(QObject):
    @pyqtSlot(int)
    def my_ageChanged_int(self, age):
        print('你的年龄是：%d'%age)

    @pyqtSlot(str)
    def my_ageChanged_str(self, ageinfo):
        print(ageinfo)

    def my_nameChanged(self, name):
        print('Hello, %s'%name)

if __name__ == "__main__":
    print('创建实例对象:')
    hunman = Human(18, '小明')
    response = Response()
    hunman.ageChanged[int].connect(response.my_ageChanged_int)
    hunman.ageChanged[str].connect(response.my_ageChanged_str)

    print('发送信号:')
    hunman.setAge(35)
    hunman.setName('大明')

    hunman.ageChanged[str].disconnect(response.my_ageChanged_str)
    print('断开连接:')
    hunman.setAge(10)