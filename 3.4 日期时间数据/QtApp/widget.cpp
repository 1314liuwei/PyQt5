#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}


void Widget::on_pushButton_GetNowTime_clicked()
{

}

void Widget::on_pushButton_SetTime_clicked()
{

}

void Widget::on_pushButton_SetDate_clicked()
{

}

void Widget::on_pushButton_SetDateTime_clicked()
{

}

void Widget::on_calendarWidget_selectionChanged()
{

}

void Widget::on_dateTimeEdit_dateChanged(const QDate &date)
{

}

void Widget::on_dateEdit_dateChanged(const QDate &date)
{

}

void Widget::on_timeEdit_dateChanged(const QDate &date)
{

}

void Widget::on_timeEdit_timeChanged(const QTime &time)
{

}
