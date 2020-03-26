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


void Widget::on_pushButton_Start_clicked()
{

}

void Widget::on_pushButton_Stop_clicked()
{

}

void Widget::on_pushButton_SetTime_clicked()
{

}
