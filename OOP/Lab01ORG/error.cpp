#include "error.h"

int show_error(const int &error)
{
    switch (error)
    {
        case FILE_OPEN_ERROR:
            QMessageBox::critical(NULL, "Error", "Can't open file");
            break;
        case MEMORY_ERROR:
            QMessageBox::critical(NULL, "Error", "Memory error");
            break;
        case NO_POINTS:
            QMessageBox::critical(NULL, "Error", "File is empty");
            break;
        case NO_LINES:
            QMessageBox::critical(NULL, "Error", "No lines");
            break;
        case UNKNOWN_COMMAND:
            QMessageBox::critical(NULL, "Error", "Command is wrong");
            break;
        default:
            QMessageBox::critical(NULL, "Error", "Error");
    }
    printf("%d\n", error);
    return OK;
}
