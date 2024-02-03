#ifndef ERROR_H
#define ERROR_H

#include <QMessageBox>

#define    OK                  0
#define    FILE_OPEN_ERROR     1
#define    DATA_ERROR          2
#define    MEMORY_ERROR        3
#define    NO_POINTS           4
#define    NO_LINES            5
#define    MODEL_NOT_LOAD      6
#define    SCENE_ERROR         7
#define    UNKNOWN_COMMAND     8

int show_error(const int &error);

#endif // ERROR_H
