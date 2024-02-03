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
    int task;
    union
    {
        const char *filename;
        drawer draw;
        move_t move;
        scale_t scale;
        rotate_t rotate;
    };
};

int request(command &data);
#endif // MENU_H
