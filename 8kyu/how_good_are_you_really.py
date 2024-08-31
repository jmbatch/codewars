# There was a test in your class and you passed it. Congratulations!

# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return true if you're better, else false!

# Note:
# Your points are not included in the array of your class's points. Do not forget them when calculating the average score!


def better_than_average(class_points, your_points):
    n = 0
    for p in class_points:
        n = n + p
    n = n + your_points
    n = n / (len(class_points) + 1)
    return your_points > n
