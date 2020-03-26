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
    void on_pushButton_GetNowTime_clicked();

    void on_pushButton_SetTime_clicked();

    void on_pushButton_SetDate_clicked();

    void on_pushButton_SetDateTime_clicked();

    void on_calendarWidget_selectionChanged();

    void on_dateTimeEdit_dateChanged(const QDate &date);

    void on_dateEdit_dateChanged(const QDate &date);

    void on_timeEdit_dateChanged(const QDate &date);

    void on_timeEdit_timeChanged(const QTime &time);

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
