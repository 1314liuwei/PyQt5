# -*- encoding: utf-8 -*-
'''
@文件 : demo.py
@Time : 2020/03/15 09:51:09
@QQ :1044945158
@Version : 3.7
'''


class hh(object):
    pass

class hhh(object):
    def __new__(cls, *args, **kwargs):
        return hh.__new__(cls, *args, **kwargs)


class Demo(list):
    nameCls = 'Demo'

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        super().__init__()
        self.name = 'Python'
        self._name = 'Python1'
        self.__name = 'Python2'

    def say(self):
        print(self.name)
        print(self._name)
        print(self.__name)

    @property
    def Name(self):
        return self._name

    @Name.setter
    def setName(self, newName):
        self._name = newName

    @classmethod
    def className(cls):
        print(f'Class Name is {cls}')

    @staticmethod
    def fun(value):
        print(value)

if __name__ == "__main__":
    demo = Demo()
    # ---------------------
    print(demo.name)
    print(demo._name)
    print(demo._Demo__name)
    # ---------------------
    print(demo.Name)
    demo.setName = 'Python3'
    print(demo.Name)
    # ---------------------
    print(demo.nameCls)
    print(Demo.nameCls)
    # ---------------------
    demo.className()
    Demo.className()
    # ---------------------
    demo.extend(['Hello', 'World'])
    print(demo)
    # ---------------------
    demo.fun('Hello')
    Demo.fun('World')
    # ---------------------
    print(isinstance(demo, Demo))
    print(isinstance(demo, list))
    a = hhh()
    print(type(a))