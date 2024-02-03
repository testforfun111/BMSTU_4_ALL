#include "menu.h"

int request(command &data)
{
    int rc = OK;
    static model_t model = model_init();

    switch (data.task)
    {
        case DOWNLOAD_FILE:
            rc = load_model(model, data.filename);
            break;
        case DRAW:
            rc = draw_model(model, data.draw);
            break;
        case MOVE:
            rc = move_model(model, data.move);
            break;
        case SCALE:
            rc = scale_model(model, data.scale);
            break;
        case ROTATE:
            rc = rotate_model(model, data.rotate);
            break;
        case END:
            model_free(model);
            break;
        default:
            rc = UNKNOWN_COMMAND;
    }

    return rc;
}
