#ifndef LINE_H
#define LINE_H

#include "points.h"
#include "error.h"

struct line {
    int point1;
    int point2;
};

using line_t = struct line;

struct lines
{
    int amount;
    line_t *arr_lines;
};
using lines_t = struct lines;

int lines_init(lines_t &lines);
int lines_allocate(lines_t &lines);
void lines_free(lines_t &lines);
int copy_lines(lines_t &lines_dst, const lines_t &lines_src);
int read_line(line_t &line, FILE *f);
int read_lines(lines_t &lines, FILE *f);
int lines_action(lines_t &lines, FILE *f);

#endif // LINE_H
