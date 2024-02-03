#ifndef DRAW_H
#define DRAW_H

#include "line.h"
#include "points.h"
#include "error.h"
#include <QGraphicsView>

struct drawer
{
    QGraphicsScene *my_scene;
    int w;
    int h;
};

struct link
{
    point_t p1;
    point_t p2;
};
typedef struct link link_t;

int change(drawer &arg, point_t &p1, point_t &p2);

link_t get_points(drawer &arg, points_t &points, line_t &line);

void my_addline(drawer &arg, point_t &p1, point_t &p2);

int my_clear(QGraphicsScene *scene);

int draw_lines(drawer &arg, points_t &points, lines_t &lines);

#endif // DRAW_H
