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


void Widget::on_checkBox_Text_clicked(bool checked)
{

}

void Widget::on_checkBox_Inverted_clicked(bool checked)
{

}

void Widget::on_radioButton_Percent_clicked()
{

}

void Widget::on_radioButton_Value_clicked()
{

}
