#include "operations.h"

void move_point(point_t &point, move_t &options)
{
    point.x += options.dx;
    point.y += options.dy;
    point.z += options.dz;
}

int move_points(points_t &points, point_t &center, move_t &options)
{
    if (points.arr_points == nullptr)
        return MODEL_NOT_LOAD;

    for (int i = 0; i < points.count; ++i)
        move_point(points.arr_points[i], options);

    move_point(center, options);
    return OK;
}

void scale(point_t &point, const double &kx, const double &ky, const double &kz)
{
    point.x = point.x * kx;
    point.y = point.y * ky;
    point.z = point.z * kz;
}

void scale_point(point_t &point, point_t &center, scale_t &options)
{
    move_to_center(point, center);
    scale(point, options.kx, options.ky, options.kz);
    move_back(point, center);
}

int scale_points(points_t &points, point_t &center, scale_t &options)
{
    if (points.arr_points == nullptr)
        return MODEL_NOT_LOAD;

    for (int i = 0; i < points.count; i++)
        scale_point(points.arr_points[i], center, options);
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

void rotate_x(point_t &point, double &alphax)
{
    double y = point.y;
    point.y = point.y * mcos(alphax) + point.z * msin(alphax);
    point.z = point.z * mcos(alphax) - y * msin(alphax);
}
void rotate_y(point_t &point, double &alphay)
{
    double x = point.x;
    point.x = point.x * mcos(alphay) + point.z * msin(alphay);
    point.z = point.z * mcos(alphay) - x * msin(alphay);
}
void rotate_z(point_t &point, double &alphaz)
{
    double x = point.x;
    point.x = point.x * mcos(alphaz) + point.y * msin(alphaz);
    point.y = point.y * mcos(alphaz) - x * msin(alphaz);
}
void rotate(point_t &point, double &alphax, double &alphay, double &alphaz)
{
    rotate_x(point, alphax);
    rotate_y(point, alphay);
    rotate_z(point, alphaz);
}

void rotate_point(point_t &point, point_t &center, double &alphax, double &alphay, double &alphaz)
{
    move_to_center(point, center);
    rotate(point, alphax, alphay, alphaz);
    move_back(point, center);
}

int rotate_points(points_t &points, point_t &center, rotate_t &options)
{
    if (points.arr_points == nullptr)
        return MODEL_NOT_LOAD;

    for (int i = 0; i < points.count; ++i)
        rotate_point(points.arr_points[i], center, options.angle_x, options.angle_y, options.angle_z);
    return OK;
}
