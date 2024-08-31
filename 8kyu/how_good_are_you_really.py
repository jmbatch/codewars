def better_than_average(class_points, your_points):
    n = 0
    for p in class_points:
        n = n + p
    n = n + your_points
    n = n / (len(class_points) + 1)
    return your_points > n
