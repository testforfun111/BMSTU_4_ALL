#ifndef MENU_H
#define MENU_H

#include "error.h"
#include "operations.h"
#include "draw.h"
#include "model.h"

#define    START          1
#define    DOWNLOAD_FILE  2
#define    DRAW           3
#define    MOVE           4
#define    SCALE          5
#define    ROTATE           6
#define    END            7

struct command
{
    int task_f;
    union
    {
        const char *filename;
        drawer draw_f;
        move_t move_f;
        scale_t scale_f;
        rotate_t rotate_f;
    };
};

int inquiry(command &data);
#endif // MENU_H
