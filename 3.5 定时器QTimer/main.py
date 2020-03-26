# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/15 11:54:00
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTime, QTimer

from widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._ui = Ui_Widget()
        self._ui.setupUi(self)

        self._timer = QTimer()
        self._timer.stop()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self.my_timer_timeout)
        self._counter = QTime()

    def on_pushButton_Start_clicked(self):
        self._timer.start()
        self._counter.start()
        self._ui.pushButton_Start.setEnabled(False)
        self._ui.pushButton_Stop.setEnabled(True)
        self._ui.pushButton_SetTime.setEnabled(False)

    
    def on_pushButton_Stop_clicked(self):
        self._timer.stop()
        tms = self._counter.elapsed()
        ms = tms % 1000
        sec = tms / 1000
        timerstr = f'当前经过时间：{sec}s {ms}ms'
        self._ui.label_Reduce.setText(timerstr)
        self._ui.pushButton_Start.setEnabled(True)
        self._ui.pushButton_Stop.setEnabled(False)
        self._ui.pushButton_SetTime.setEnabled(True)

    def on_pushButton_SetTime_clicked(self):
        self._timer.setInterval(self._ui.timeEdit.value())


    def my_timer_timeout(self):
        curTime = QTime.currentTime()
        self._ui.lcdNumber_Hour.display(curTime.hour())
        self._ui.lcdNumber_Minute.display(curTime.minute())
        self._ui.lcdNumber_Second.display(curTime.second())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())