#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}


void Dialog::on_btnClear_clicked();

void Dialog::on_chkBoxUnder_clicked();

void Dialog::on_checkBoxBold_clicked(bool checked);


void Dialog::on_radioRed_clicked()
{

}

void Dialog::on_radioBlack_clicked()
{

}

void Dialog::on_radioBlue_clicked()
{

}
