#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "ui_mainwindow.h"
#include "menu.h"

#define WIN_X 100
#define WIN_Y 100

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_name_clicked();

    void on_pushButton_move_clicked();

    void on_pushButton_turn_clicked();

    void on_pushButton_scale_clicked();

private:
    Ui::MainWindow *ui;
};

int inquiry(command &data);
int transf_show(command req, Ui::MainWindow *ui);
int start_draw(Ui::MainWindow *ui);

#endif // MAINWINDOW_H
