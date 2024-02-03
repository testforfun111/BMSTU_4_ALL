#include "model.h"

model_t &model_init(void)
{
    static model_t model;
    points_init(model.points);
    lines_init(model.lines);
    point_init(model.center);

    return model;
}

void model_free(model_t &model)
{
    points_free(model.points);
    lines_free(model.lines);
}

int copy_model(model_t &model_dst, const model_t &model_src)
{
    int rc = copy_points(model_dst.points, model_src.points);
    if (rc == OK)
    {
        copy_point(model_dst.center, model_src.center);
        rc = copy_lines(model_dst.lines, model_src.lines);
    }
    return rc;
}

int read_model(model_t &model, FILE *f)
{
    int rc = points_actions(model.points, f);
    if (rc == OK)
    {
        rc = lines_action(model.lines, f);
        if (rc != OK)
            points_free(model.points);
    }
    return rc;
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
        model_t model_temp = model_init();
        rc = read_model(model_temp, f);

        if (rc == OK)
        {
            model_free(model);
            copy_model(model, model_temp);
        }
        model_free(model_temp);
        fclose(f);
    }
    return rc;
}

int draw_model(model_t &model, drawer &arg)
{
    if (model.points.count == 0)
        return NO_POINTS;

    int rc = OK;
    rc = my_clear(arg.my_scene);
    if (rc == OK)
        rc = draw_lines(arg, model.points, model.lines);

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
