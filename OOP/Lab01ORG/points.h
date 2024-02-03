#ifndef POINTS_H
#define POINTS_H

#include <cstdio>
#include <cstdlib>
#include "error.h"

struct point {
    double x;
    double y;
    double z;
};

typedef struct point point_t;

struct points {
    int count;
    point_t *arr_points;
};

typedef struct points points_t;

void points_init(points_t &points);
void point_init(point_t &point);
int read_amount(int &n, FILE *f);
void copy_point(point_t &point_dst, const point_t &point_src);
int copy_points(points_t &points_dst, const points_t &points_src);
int read_point(point_t &point, FILE *f);
int read_points(points_t &arr_points, FILE *f);
int points_allocate(points_t &arr_points);
void points_free(points_t &arr_points);
int points_actions(points_t &arr_points, FILE *f);

#endif // POINTS_H
