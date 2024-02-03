#ifndef MODEL_H
#define MODEL_H

#include "points.h"
#include "line.h"
#include "error.h"
#include "draw.h"
#include "operations.h"

struct model
{
    points_t points;
    lines_t lines;
    point_t center;
};

using model_t = struct model;

model_t &model_init(void);

void model_free(model_t &model);

int copy_model(model_t &model_dst, const model_t &model_src);

int read_model(model_t &model, FILE *f);

int load_model(model_t &model, const char *filename);

int draw_model(model_t &model, drawer &arg);

int move_model(model_t &model, move_t &options);

int scale_model(model_t &model, scale_t &options);

int rotate_model(model_t &model, rotate_t &options);

#endif // MODEL_H
