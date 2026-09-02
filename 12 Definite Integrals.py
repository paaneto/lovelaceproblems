def area_of_rectangles(rects, dx):
    area = 0

    for k in range(len(rects)):
        area += rects[k]*dx

    return area

print(area_of_rectangles([0, 1, 2, 3, 4, 5], 1.5))
#output = 22.5