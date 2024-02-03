#ifndef OPERATIONS_H
#define OPERATIONS_H

#include "error.h"
#include "line.h"
#include "points.h"
#include <cmath>

struct move
{
    double dx;
    double dy;
    double dz;
};

typedef struct move move_t;

struct rotate
{
    double angle_x;
    double angle_y;
    double angle_z;
};
typedef struct rotate rotate_t;

struct scale
{
    double kx;
    double ky;
    double kz;
};
typedef struct scale scale_t;

int move_points(points_t &points, point_t &center, move_t &options);
void scale(point_t &point, const double &kx, const double &ky, const double &kz);
void scale_point(point_t &point, point_t &center, scale_t &options);
int scale_points(points_t &points, point_t &center, scale_t &options);
double msin(const double &alpha);
double mcos(const double &alpha);
void move_to_center(point_t &point, point_t &center);
void move_back(point_t &point, point_t &center);
void rotate(point_t &point, double &alphax, double &alphay, double &alphaz);
void rotate_point(point_t &point, point_t &center, double &alphax, double &alphay, double &alphaz);
int rotate_points(points_t &points, point_t &center, rotate_t &options);
#endif // OPERATIONS_H
