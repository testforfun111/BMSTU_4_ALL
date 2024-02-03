#include "model.h"

model_t &model_init(void)
{
    static model_t model;
    points_init(model.points);
    lines_init(model.lines);
    point_init(model.center);

    return model;
}

void free_model_component(points_t &points, lines_t &lines)
{
    points_free(points);
    lines_free(lines);
}

void model_free(model_t &model)
{
    free_model_component(model.points, model.lines);
}

int read_model_component(points_t &points, lines_t &lines, FILE *f)
{
    int rc = points_actions(points, f);
    if (rc == OK)
    {
        rc = lines_action(lines, f);
        if (rc != OK)
            points_free(points);
    }
    return rc;
}

int read_model(model_t &model, FILE *f)
{
    model = model_init();
    return read_model_component(model.points, model.lines, f);
}

int load_model(model_t &model, const char *filename)
{
    if (filename == nullptr)
        return FILE_OPEN_ERROR;

    int rc = OK;
    FILE *f = fopen(filename, "r");
    if (!f)
        rc = FILE_OPEN_ERROR;
    else
    {
        model_t model_temp;
        rc = read_model(model_temp, f);
        fclose(f);
        if (rc == OK)
        {
            model_free(model);
            model = model_temp;
        }
    }
    return rc;
}

int draw_model(model_t &model, drawer &arg)
{
    if (model.points.count == 0)
        return NO_POINTS;
    int rc = OK;
    points_t points_tranfer;

    convert_points_to_draw(points_tranfer, model.points, arg);

    my_clear(arg.my_scene);
    if (rc == OK)
        rc = draw_lines(arg, points_tranfer, model.lines);

    points_free(points_tranfer);
    return rc;
}

int move_model(model_t &model, move_t &options)
{
    return move_points(model.points, model.center, options);
}

int scale_model(model_t &model, scale_t &options)
{
    return scale_points(model.points, model.center, options);
}

int rotate_model(model_t &model, rotate_t &options)
{
    return rotate_points(model.points, model.center, options);
}
