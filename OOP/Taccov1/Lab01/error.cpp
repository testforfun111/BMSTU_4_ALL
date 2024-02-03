#include "error.h"

int show_error(const int &error)
{
    switch (error)
    {
        case FILE_OPEN_ERROR:
            QMessageBox::critical(nullptr, "Error", "Can't open file");
            break;
        case MEMORY_ERROR:
            QMessageBox::critical(nullptr, "Error", "Memory error");
            break;
        case NO_POINTS:
            QMessageBox::critical(nullptr, "Error", "File is empty");
            break;
        case NO_LINES:
            QMessageBox::critical(nullptr, "Error", "No lines");
            break;
        case UNKNOWN_COMMAND:
            QMessageBox::critical(nullptr, "Error", "Command is wrong");
            break;
        default:
            QMessageBox::critical(nullptr, "Error", "Error");
    }
    printf("%d\n", error);
    return OK;
}
