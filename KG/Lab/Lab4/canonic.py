from draw_pixel import draw_simetric_pixels
import math as m
# (x - xc) ** 2 + (y - yc) ** 2 = R**2
# f(x, y) = (x - xc) ** 2 + (y - yc) ** 2 - R**2
# y = yc + sqrt(R**2 - (x - xc)**2)
# x = xc + sqrt(R**2 - (y - yc)**2)
def canonical_сircle(canvas, xc, yc, r, colour, draw):
    sqr_r = r ** 2

    quarter = round(xc + r / m.sqrt(2))

    for x in range(xc, quarter + 1):
        y = yc + round(m.sqrt(sqr_r - (x - xc) ** 2))
        if draw:
            draw_simetric_pixels(canvas, [x, y, colour], xc, yc, circle=True)


def canonical_ellipse(canvas, xc, yc, ra, rb, colour, draw):
    sqr_ra = ra * ra 
    sqr_rb = rb * rb

    quarter_x = round(xc + ra / m.sqrt(1 + sqr_rb / sqr_ra))
    quarter_y = round(yc + rb / m.sqrt(1 + sqr_ra / sqr_rb))
    # print(quarter_x, quarter_y, xc, yc)
    for x in range(xc, quarter_x + 1):
        y = yc + round(m.sqrt(sqr_ra * sqr_rb - (x - xc) ** 2 * sqr_rb) / ra)

        if draw:
            draw_simetric_pixels(canvas, [x, y, colour], xc, yc, circle=False)

    for y in range(quarter_y, yc - 1, -1):
        x = xc + round(m.sqrt(sqr_ra * sqr_rb - (y - yc) ** 2 * sqr_ra) / rb)

        if draw:
            draw_simetric_pixels(canvas, [x, y, colour], xc, yc, circle=False)