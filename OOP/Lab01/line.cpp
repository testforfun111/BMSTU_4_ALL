#include "line.h"

void lines_init(lines_t &lines)
{
    lines.amount = 0;
    lines.arr_lines = nullptr;
}

int lines_allocate(lines_t &lines)
{
    int rc = OK;
    lines.arr_lines = (line_t *) malloc(sizeof(line_t) * lines.amount);
    if (lines.arr_lines == nullptr)
        rc = MEMORY_ERROR;
    return rc;
}

void lines_free(lines_t &lines)
{
    lines.amount = 0;
    if (lines.arr_lines)
    {
        free(lines.arr_lines);
        lines.arr_lines = nullptr;
    }
}

int read_line(line_t &line, FILE *f)
{
    if (f == nullptr)
        return FILE_OPEN_ERROR;

    int rc = OK;
    if (fscanf(f, "%d%d", &line.point1, &line.point2) != 2)
        rc = DATA_ERROR;
    return rc;
}

int read_lines(lines_t &lines, FILE *f)
{
    if (lines.arr_lines == nullptr)
        return MEMORY_ERROR;

    if (f == nullptr)
        return FILE_OPEN_ERROR;

    int rc = OK;
    for (int i = 0; rc == OK && i < lines.amount; i++)
        rc = read_line(lines.arr_lines[i], f);
    return rc;
}

int lines_action(lines_t &lines, FILE *f)
{
    if (f == nullptr)
        return FILE_OPEN_ERROR;

    int rc = read_amount(lines.amount, f);
    if (rc == OK)
        rc = lines_allocate(lines);

    if (rc == OK)
    {
        rc = read_lines(lines, f);
        if (rc != OK)
            lines_free(lines);
    }
    return rc;
}
