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


void Widget::on_pushButton_Left_clicked()
{

}

void Widget::on_pushButton_Center_clicked()
{

}

void Widget::on_pushButton_Right_clicked()
{

}

void Widget::on_pushButton_Bold_clicked(bool checked)
{

}

void Widget::on_pushButton_Italic_clicked(bool checked)
{

}

void Widget::on_pushButton_Underline_clicked(bool checked)
{

}

void Widget::on_checkBox_ReadOnly_clicked(bool checked)
{

}

void Widget::on_checkBox_EnaBled_clicked(bool checked)
{

}

void Widget::on_checkBox_ClearButtonEnabled_clicked(bool checked)
{

}
