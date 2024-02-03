#include "draw.h"

void change_point(point_t &point, drawer &arg)
{
    point.x = point.x + arg.w / 2;
    point.y = point.y + arg.h / 2;
}

void change_points(points_t &points, drawer &arg)
{
    for (int i = 0; i < points.count; i++)
        change_point(points.arr_points[i], arg);
}

link_t get_points(points_t &points, line_t &line)
{
    static link_t link;
    link.p1 = points.arr_points[line.point1];
    link.p2 = points.arr_points[line.point2];

    return link;
}

void my_addline(drawer &arg, point_t &p1, point_t &p2)
{

    arg.my_scene->addLine(p1.x, p1.y, p2.x, p2.y);
}

int my_clear(QGraphicsScene *scene)
{
    scene->clear();
    return OK;
}

int draw_lines(drawer &arg, points_t &points, lines_t &lines)
{
    int rc = OK;
    if (points.arr_points == nullptr || lines.arr_lines == nullptr)
            rc = MEMORY_ERROR;
    else
    {
        link_t link;
        for (int i = 0; i < lines.amount; i++)
        {
            link = get_points(points, lines.arr_lines[i]);
            my_addline(arg, link.p1, link.p2);
        }
    }
    return rc;
}

