# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/15 11:26:03
@QQ :1044945158
@Version : 3.7
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, QTime, QDate, QDateTime

from widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._ui = Ui_Widget()
        self._ui.setupUi(self)

    def on_pushButton_GetNowTime_clicked(self):
        curDateTime = QDateTime.currentDateTime()
        self._ui.timeEdit.setTime(curDateTime.time())
        self._ui.lineEdit_Time.setText(curDateTime.toString('hh:mm:ss'))
        self._ui.dateEdit.setDate(curDateTime.date())
        self._ui.lineEdit_Date.setText(curDateTime.toString('yyyy/MM/dd'))
        self._ui.dateTimeEdit.setDateTime(curDateTime)
        self._ui.lineEdit_DateTime.setText(curDateTime.toString('yyyy/MM/dd hh:mm:ss'))
    
    def on_pushButton_SetTime_clicked(self):
        tmStr = self._ui.lineEdit_Time.text()
        tm = QTime.fromString(tmStr, 'hh:mm:ss')
        self._ui.timeEdit.setTime(tm)
    
    def on_pushButton_SetDate_clicked(self):
        dtStr = self._ui.lineEdit_Date.text()
        dt = QDate.fromString(dtStr, 'yyyy/MM/dd')
        self._ui.dateEdit.setDate(dt)
    
    def on_pushButton_SetDateTime_clicked(self):
        dttmStr = self._ui.lineEdit_DateTime.text()
        dttm = QDateTime.fromString(dttmStr, 'yyyy/MM/dd hh:mm:ss')
        self._ui.dateTimeEdit.setDateTime(dttm)
    
    def on_calendarWidget_selectionChanged(self):
        date = self._ui.calendarWidget.selectedDate()
        self._ui.lineEdit_Search.setText(date.toString('yyyy年MM月dd日'))

    def on_dateTimeEdit_dateChanged(self, dateTime):
        self._ui.lineEdit_DateTime.setText(dateTime.toString('yyyy/MM/dd hh:mm:ss'))

    def on_dateEdit_dateChanged(self, date):
        self._ui.lineEdit_Date.setText(date.toString('yyyy/MM/dd'))

    def on_timeEdit_timeChanged(self, time):
        self._ui.lineEdit_Time.setText(time.toString('hh:mm:ss'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())

    
