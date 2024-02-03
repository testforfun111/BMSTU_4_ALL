def set_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill=color, width=1)

def draw_simetric_pixels(canvas, dot, xc, yc, circle=True):
    if circle:
        set_pixel(canvas,  dot[1] - yc + xc,  dot[0] - xc + yc, dot[2]) # через y = x
        set_pixel(canvas, -dot[1] + yc + xc,  dot[0] - xc + yc, dot[2]) # 2
        set_pixel(canvas,  dot[1] - yc + xc, -dot[0] + xc + yc, dot[2]) # 4
        set_pixel(canvas, -dot[1] + yc + xc, -dot[0] + xc + yc, dot[2]) # 3

    set_pixel(canvas,  dot[0],           dot[1],          dot[2])       # 
    set_pixel(canvas, -dot[0] + 2 * xc,  dot[1],          dot[2])       # через Oy
    set_pixel(canvas,  dot[0],          -dot[1] + 2 * yc, dot[2])       # через Ox
    set_pixel(canvas, -dot[0] + 2 * xc, -dot[1] + 2 * yc, dot[2])       # через O'