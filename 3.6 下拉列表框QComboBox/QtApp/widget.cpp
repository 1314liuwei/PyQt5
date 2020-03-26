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


void Widget::on_pushButton_InitList_clicked()
{

}

void Widget::on_pushButton_ClearList_clicked()
{

}

void Widget::on_pushButton_InitCity_clicked()
{

}

void Widget::on_checkBox_clicked(bool checked)
{

}

void Widget::on_comboBox_City_currentIndexChanged(const QString &arg1)
{

}

void Widget::on_comboBox_User_currentIndexChanged(const QString &arg1)
{

}
