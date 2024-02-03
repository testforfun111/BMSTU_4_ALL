# Массив цветов одного оттенка разной интенсивности
def get_rgb_intensity(color, bg_color, intensity):
    grad = []
    r_ratio = float(bg_color[0] - color[0]) / intensity # получение шага интенсивности
    g_ratio = float(bg_color[1] - color[1]) / intensity
    b_ratio = float(bg_color[2] - color[2]) / intensity
    for i in range(intensity):
        nr = int(color[0] + (r_ratio * i)) # заполнение массива разными оттенками
        ng = int(color[1] + (g_ratio * i))
        nb = int(color[2] + (b_ratio * i))
        grad.append("#%2.2x%2.2x%2.2x" % (nr, ng, nb))
    # grad.reverse()
    return grad
