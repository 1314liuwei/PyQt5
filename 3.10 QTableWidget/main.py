# -*- encoding: utf-8 -*-
'''
@文件 : main.py
@Time : 2020/03/23 15:47:21
@QQ :1044945158
@Version : 3.7
'''

import sys
from enum import Enum

from PyQt5.QtCore import QDate, Qt, pyqtSlot
from PyQt5.QtGui import QBrush, QFont, QIcon
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QLabel,
                             QMainWindow, QTableWidgetItem)

from mainwindow import Ui_MainWindow


class CellType(Enum):  # 单元格的类型
    ctName = 1000
    ctSex = 1001
    ctBirth = 1002
    ctNation = 1003
    ctScore = 1004
    ctPartyM = 1005


class FieldColNum(Enum):  # 各个字段在表格中的列号
    colName = 0
    colSex = 1
    colBirth = 2
    colNation = 3
    colScore = 4
    colPartM = 5


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # 创建Label标签
        self.LabCellIndex = QLabel('当前单元格坐标：', self)
        self.LabCellIndex.setMinimumWidth(250)
        self.LabCellType = QLabel('当前单元格类型：', self)
        self.LabCellType.setMinimumWidth(200)
        self.LabStudID = QLabel('学生ID：',self)
        self.LabStudID.setMinimumWidth(200)

        # 添加到状态栏
        self._ui.statusbar.addWidget(self.LabCellIndex)
        self._ui.statusbar.addWidget(self.LabCellType)
        self._ui.statusbar.addWidget(self.LabStudID)

        self._ui.tableWidget.setAlternatingRowColors(True)  # 交替行颜色
        self.__tableInitialized = False  # 表格数据是否初始化标识

    # 设置表头
    def on_pushButton_setTableHead_clicked(self):
        headerText = ['姓 名', '性 别', '出生日期', '民 族', '分 数', '是否党员']
        self._ui.tableWidget.setColumnCount(len(headerText))
        for i, info in enumerate(headerText):
            headerItem = QTableWidgetItem(info)
            font = headerItem.font()
            font.setPointSize(11)
            headerItem.setFont(font)
            headerItem.setBackground(QBrush(Qt.red))
            self._ui.tableWidget.setHorizontalHeaderItem(i, headerItem)

    # 设置行数
    def on_pushButton_setRowNum_clicked(self):
        self._ui.tableWidget.setRowCount(self._ui.spinBox.value())
        self._ui.tableWidget.setAlternatingRowColors(self._ui.checkBox_setColor.isChecked())

    
    def on_pushButton_initTableData_clicked(self):
        """初始化表格数据

        生产每一行的信息
        利用__createItemsARow()创建行
        将__tableInitialized 置为True
        """
        self._ui.tableWidget.clearContents()  # 清除表格内容
        birth = QDate(2000, 1, 20)
        isParty = True
        nation = '汉'
        score = 99

        rowCount = self._ui.tableWidget.rowCount()  # 表格行数
        for i in range(rowCount):
            name = f'学生：{i}'
            sex = '女' if i%2 else '男'
            self.__createItemsARow(i, name, sex, birth, nation, isParty, score)  # 创建行
            birth = birth.addDays(20)
            isParty = not isParty

        self.__tableInitialized = True  # 表格数据初始化标识设置为True

        
    def __createItemsARow(self, rowNo, name, sex, birth, nation, isParty, score):
        """创建行

        :param rowNo: 行号
        :param name: 学生名字
        :param sex: 学生性别
        :param birth: 出生日期
        :param nation: 民族
        :param isParty: 是否为党员
        :param score: 得分
        :return: None
        """
        ID = 2018101000 + rowNo  # 学号

        # 姓名
        item = QTableWidgetItem(name, CellType.ctName.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置对齐方式
        font = item.font()  # 设置字体
        font.setBold(True)
        item.setFont(font)
        item.setData(Qt.UserRole, ID)  # 关联数据
        self._ui.tableWidget.setItem(rowNo, FieldColNum.colName.value, item)  # 创建姓名单元格

        # 性别
        if sex == '男':
            icon = QIcon(':icon/images/boy.ico')  # 设置图标
        else:
            icon = QIcon(':icon/images/girl.ico')
        item = QTableWidgetItem(sex, CellType.ctSex.value)
        item.setIcon(icon)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self._ui.tableWidget.setItem(rowNo, FieldColNum.colSex.value, item)  # 创建性别单元格

        # 生日
        strBirth = birth.toString('yyyy-MM-dd')  # 将时间转换成字符串
        item = QTableWidgetItem(strBirth, CellType.ctBirth.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self._ui.tableWidget.setItem(rowNo, FieldColNum.colBirth.value, item)  # 创建生日单元格

        # 民族
        item = QTableWidgetItem(nation, CellType.ctNation.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if nation != '汉':
            item.setForeground(QBrush(Qt.blue))
        self._ui.tableWidget.setItem(rowNo, FieldColNum.colNation.value, item)  # 创建民族单元格

        # 得分
        item = QTableWidgetItem(str(score), CellType.ctScore.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self._ui.tableWidget.setItem(rowNo, FieldColNum.colScore.value, item)  # 创建得分单元格

        # 是否是党员
        item = QTableWidgetItem('党员', CellType.ctPartyM.value)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if isParty:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setBackground(QBrush(Qt.yellow))
        self._ui.tableWidget.setItem(rowNo, FieldColNum.colPartM.value, item)  # 创建是否是党员单元格

    @pyqtSlot(int, int, int, int)
    def on_tableWidget_currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        """当前单元格发生变化
        """
        if not self.__tableInitialized:
            return
        item = self._ui.tableWidget.item(currentRow, currentColumn)

        self.LabCellIndex.setText(f'当前单元格：{currentRow}行，{currentColumn}列')
        itemCellType = item.type()
        self.LabCellType.setText(f'当前单元格类型：{itemCellType}')

        item1 = self._ui.tableWidget.item(currentRow, FieldColNum.colName.value)
        studID = item1.data(Qt.UserRole)
        self.LabStudID.setText(f'学生ID：{studID}')

    def on_pushButton_insertRow_clicked(self):
        """插入行
        """
        curRow = self._ui.tableWidget.currentRow()
        self._ui.tableWidget.insertRow(curRow)
        birth = QDate.fromString('2000-4-5', 'yyyy-M-d')
        self.__createItemsARow(curRow, '新学生', '男', birth, '苗族', True, 65)

    def on_pushButton_addRow_clicked(self):
        """添加行
        """
        curRow = self._ui.tableWidget.currentRow()
        self._ui.tableWidget.insertRow(curRow)
        birth = QDate.fromString('1998-4-5', 'yyyy-M-d')
        self.__createItemsARow(curRow, '新学生', '女', birth, '苗族', True, 56)

    def on_pushButton_deleteRow_clicked(self):
        """删除行
        """
        curRow = self._ui.tableWidget.currentRow()
        self._ui.tableWidget.removeRow(curRow)

    def on_pushButton_clearRow_clicked(self):
        """清除单元格内容
        """
        self._ui.tableWidget.clearContents()

    def on_pushButton_autoRowHeight_clicked(self):
        """自动设置行高
        """
        self._ui.tableWidget.resizeRowsToContents()

    def on_pushButton_autoColWidth_clicked(self):
        """自动设置列宽
        """
        self._ui.tableWidget.resizeColumnsToContents()

    @pyqtSlot(bool)
    def on_checkBox_editAbled_clicked(self, checked):
        """表格可编辑
        """
        trig = (QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked) if checked else QAbstractItemView.NoEditTriggers
        self._ui.tableWidget.setEditTriggers(trig)

    @pyqtSlot(bool)
    def on_checkBox_diaplayRowHead_clicked(self, checked):
        """是否显示行表头
        """
        self._ui.tableWidget.horizontalHeader().setVisible(checked)

    @pyqtSlot(bool)
    def on_checkBox_setColHead(self, checked):
        """是否显示列表头
        """
        self._ui.tableWidget.verticalHeader().setVisible(checked)

    @pyqtSlot(bool)
    def on_checkBox_setColor_clicked(self, checked):
        """间隔行底色
        """
        self._ui.tableWidget.setAlternatingRowColors(checked)

    def on_radioButton_row_clicked(self):
        """选择模式：行选择
        """
        selMode = QAbstractItemView.SelectRows
        self._ui.tableWidget.setSelectionBehavior(selMode)

    def on_radioButton_col_clicked(self):
        """选择模式：单元格选择
        """
        selMode = QAbstractItemView.SelectItems
        self._ui.tableWidget.setSelectionBehavior(selMode)

    def on_pushButton_readTable_clicked(self):
        """读取表格到文本
        """
        self._ui.plainTextEdit.clear()
        rowCount = self._ui.tableWidget.rowCount()
        colCount = self._ui.tableWidget.columnCount()
        for i in range(rowCount):
            strText = f'第{i + 1}行:'
            for j in range(colCount - 1):
                cellItem = self._ui.tableWidget.item(i, j)
                strText = strText + cellItem.text() + ' | '
            cellItem = self._ui.tableWidget.item(i, colCount - 1)
            strText = strText + '党员' if cellItem.checkState() == Qt.Checked else strText + '群众'
            self._ui.plainTextEdit.appendPlainText(strText)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())