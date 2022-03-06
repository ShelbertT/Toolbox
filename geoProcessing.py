import math


def get_shape_length(polygon):  # list[list[x, y]] -> double | calculate the perimeter of a polygon based on its [converted coords]
    perimeter = 0
    for i in range(len(polygon)):
        start = i
        if start == len(polygon)-1:
            end = 0
        else:
            end = i + 1

        this_line = math.sqrt(math.pow((polygon[start][0] - polygon[end][0]), 2) + math.pow((polygon[start][1] - polygon[end][1]), 2))
        perimeter += this_line

    return perimeter


def get_shape_area(polygon):  # list[list[x, y]] -> double | calculate the area of a polygon based on its [converted coords]
    # Calculation is based on [Shoelace Theorem]
    area = 0
    for i in range(len(polygon)):
        current = i
        if current == len(polygon)-1:
            next_one = 0
        else:
            next_one = i+1
        area += (polygon[current][0] * polygon[next_one][1]) - (polygon[next_one][0] * polygon[current][1])

    area = abs(area) / 2
    return area