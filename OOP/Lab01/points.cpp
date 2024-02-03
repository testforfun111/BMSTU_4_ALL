#include "points.h"

void point_init(point_t &point)
{
    point.x = 0.0;
    point.y = 0.0;
    point.z = 0.0;
}

void points_init(points_t &points)
{
    points.count = 0;
    points.arr_points = nullptr;
}

void copy_point(point_t &point_dst, const point_t &point_src)
{
    point_dst.x = point_src.x;
    point_dst.y = point_src.y;
    point_dst.z = point_src.z;
}

int read_amount(int &n, FILE *f)
{
    if (f == nullptr)
        return FILE_OPEN_ERROR;

    int rc = OK;
    if (fscanf(f, "%d", &n) != 1 || n <= 0)
        rc = DATA_ERROR;
    return rc;
}

int read_point(point_t &point, FILE *f)
{
    if (!f)
        return FILE_OPEN_ERROR;

    int rc = OK;
    if (fscanf(f, "%lf%lf%lf", &point.x, &point.y, &point.z) != 3)
        rc = DATA_ERROR;
    return rc;
}

int read_points(points_t &points, FILE *f)
{
    if (points.arr_points == nullptr)
        return MEMORY_ERROR;
    if (f == nullptr)
        return FILE_OPEN_ERROR;

    int rc = OK;
    for (int i = 0; rc == OK && i < points.count; i++)
        rc = read_point(points.arr_points[i], f);
    return rc;
}

int points_allocate(points_t &points)
{
    int rc = OK;
    points.arr_points = (point_t *) malloc(sizeof(point_t) * points.count);
    if (points.arr_points == nullptr)
        rc = MEMORY_ERROR;
    return rc;
}

void points_free(points_t &points)
{
    points.count = 0;
    if (points.arr_points)
    {
        free(points.arr_points);
        points.arr_points = nullptr;
    }
}

int points_actions(points_t &points, FILE *f)
{
    if (f == nullptr)
        return FILE_OPEN_ERROR;

    int rc = read_amount(points.count, f);
    if (rc == OK)
        rc = points_allocate(points);

    if (rc == OK)
    {
        rc = read_points(points, f);
        if (rc != OK)
            points_free(points);
    }
    return rc;
}
