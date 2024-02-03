#include "operations.h"

int scale_points(points_t &points, point_t center, scale_t &options)
{
    if (points.arr_points == NULL)
        return MODEL_NOT_LOAD;
    for (int i = 0; i < points.count; i++)
    {
        points.arr_points[i].x = points.arr_points[i].x * options.kx + (1 - options.kx) * center.x;
        points.arr_points[i].y = points.arr_points[i].y * options.ky + (1 - options.ky) * center.y;
        points.arr_points[i].z = points.arr_points[i].z * options.kz + (1 - options.kz) * center.z;
    }
    return OK;
}

double msin(const double &alpha)
{
    return sin(alpha * M_PI / 360);
}

double mcos(const double &alpha)
{
    return cos(alpha * M_PI / 360);
}

void move_to_center(point_t &point, point_t &center)
{
    point.x -= center.x;
    point.y -= center.y;
    point.z -= center.z;
}

void move_back(point_t &point, point_t &center)
{
   point.x += center.x;
   point.y += center.y;
   point.z += center.z;
}

void rotate(point_t &point, const double &alphax, const double &alphay, const double &alphaz)
{
    // double x = point.x;
    // double y = point.y;
    // double z = point.z;
    point.y = point.y * mcos(alphax) + point.z * msin(alphax);
    point.z = point.z * mcos(alphax) - point.y * msin(alphax);

    point.x = point.x * mcos(alphay) + point.z * msin(alphay);
    point.z = point.z * mcos(alphay) - point.x * msin(alphay);

    point.x = point.x * mcos(alphaz) + point.y * msin(alphaz);
    point.y = point.y * mcos(alphaz) - point.x * msin(alphaz);
}


void rotate_point(point_t &point, point_t &center, const double &alphax, const double &alphay, const double &alphaz)
{
    move_to_center(point, center);
    rotate(point, alphax, alphay, alphaz);
    move_back(point, center);
}

int rotate_points(points_t &points, point_t &center, rotate_t &options)
{
    if (points.arr_points == NULL)
        return MODEL_NOT_LOAD;

    for (int i = 0; i < points.count; ++i)
        rotate_point(points.arr_points[i], center, options.angle_x, options.angle_y, options.angle_z);

    return OK;
}

int move_points(points_t &points, point_t &center, const move_t &options)
{
    if (points.arr_points == NULL)
        return MODEL_NOT_LOAD;

    for (int i = 0; i < points.count; ++i)
    {
        points.arr_points[i].x += options.dx;
        points.arr_points[i].y += options.dy;
        points.arr_points[i].z += options.dz;
    }
    center.x += options.dx;
    center.y += options.dy;
    center.z += options.dz;

    return OK;
}

