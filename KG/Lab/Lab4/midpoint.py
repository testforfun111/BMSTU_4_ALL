from draw_pixel import draw_simetric_pixels, set_pixel
import math as m


# f(x, y) = f(r - 1/2, 0)
def midpoint_circle(canvas, xc, yc, r, colour, draw=True):
    y = r 
    x = 0

    if draw:
        draw_simetric_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=True)

    delta = 1 - r  # 5/4 - r

    while y >= x:
        if delta >= 0:
            y -= 1
            x += 1
            delta += 2 * x + 1 - 2 * y
        else:
            x += 1
            delta += 2 * x + 1

        if draw:
            draw_simetric_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=True)


def midpoint_ellipse(canvas, xc, yc, ra, rb, colour, draw=True):
    sqr_ra = ra * ra
    sqr_rb = rb * rb

    x = 0
    y = rb

    if draw:
        draw_simetric_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=False)

    border = round(ra / m.sqrt(1 + sqr_rb / sqr_ra))
    delta = sqr_rb - round(sqr_ra * (rb - 1 / 4))

    while x <= border:
        if delta < 0:
            x += 1
            delta += 2 * sqr_rb * x + sqr_rb
        else:
            x += 1
            y -= 1
            delta += 2 * sqr_rb * x - 2 * sqr_ra * y + sqr_rb

        if draw:
            draw_simetric_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=False)

    x = ra
    y = 0

    if draw:
        draw_simetric_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=False)

    border = round(rb / m.sqrt(1 + sqr_ra / sqr_rb))
    delta = sqr_ra - round(sqr_rb * (ra - 1 / 4))

    while y <= border:
        if delta < 0:
            y += 1
            delta += 2 * sqr_ra * y + sqr_ra
        else:
            x -= 1
            y += 1
            delta += 2 * sqr_ra * y - 2 * sqr_rb * x + sqr_ra

        if draw:
            draw_simetric_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=False)

