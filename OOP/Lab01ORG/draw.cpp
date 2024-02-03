#include "draw.h"

int change(drawer &arg, point_t &p1, point_t &p2)
{
    p1.x = p1.x + arg.w / 2;
    p1.y = p1.y + arg.h / 2;

    p2.x = p2.x + arg.w / 2;
    p2.y = p2.y + arg.h / 2;

    return OK;
}

link_t get_points(drawer &arg, points_t &points, line_t &line)
{
    link_t link;
    link.p1 = points.arr_points[line.point1];
    link.p2 = points.arr_points[line.point2];

    change(arg, link.p1, link.p2);
    return link;
}

void my_addline(drawer &arg, point_t &p1, point_t &p2)
{

    arg.my_scene->addLine(p1.x, p1.y, p2.x, p2.y);
}

int my_clear(QGraphicsScene *scene)
{
    scene->addText("fsdlkfjs");
    scene->clear();
    return OK;
}

int draw_lines(drawer &arg, points_t &points, lines_t &lines)
{
    int rc = OK;
    if (points.arr_points == NULL || lines.arr_lines == NULL)
            rc = MEMORY_ERROR;
    else
    {
        link_t link;
        for (int i = 0; rc == OK && i < lines.amount; i++)
        {
            link = get_points(arg, points, lines.arr_lines[i]);
            my_addline(arg, link.p1, link.p2);
        }
    }
    return rc;
}

