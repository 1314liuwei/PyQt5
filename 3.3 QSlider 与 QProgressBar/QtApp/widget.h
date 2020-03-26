#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_checkBox_Text_clicked(bool checked);

    void on_checkBox_Inverted_clicked(bool checked);

    void on_radioButton_Percent_clicked();

    void on_radioButton_Value_clicked();

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
