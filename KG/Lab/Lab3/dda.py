
def dda(start_point, end_point, color):
    
    dx = (end_point[0] - start_point[0])
    dy = (end_point[1] - start_point[1])

    if dx == 0 and dy == 0:
        return [[round(start_point[0]), round(start_point[1]), color]]

    l = max(abs(dx), abs(dy))
    dx /= l
    dy /= l

    x = start_point[0]
    y = start_point[1]

    points = [[round(x), round(y), color]]

    i = 0
    while i <= l:
        x += dx
        y += dy

        points.append([round(x), round(y), color])
        i += 1
        
    return points

