#include "menu.h"

int inquiry(command &data)
{
    int rc = OK;
    static model_t model = model_init();

    switch (data.task_f)
    {
        case START:
            break;
        case DOWNLOAD_FILE:
            rc = load_model(model, data.filename);
            break;
        case DRAW:
            rc = draw_model(model, data.draw_f);
            break;
        case MOVE:
            rc = move_model(model, data.move_f);
            break;
        case SCALE:
            rc = scale_model(model, data.scale_f);
            break;
        case ROTATE:
            rc = rotate_model(model, data.rotate_f);
            break;
        case END:
            model_free(model);
            break;
        default:
            rc = UNKNOWN_COMMAND;
    }

    return rc;
}
