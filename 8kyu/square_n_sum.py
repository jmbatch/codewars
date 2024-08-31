# Complete the square sum function so that it squares each number passed into it and then sums the results together.


def square_sum(numbers):
    x = 0
    for i in numbers:
        i = i**2
        x = i + x
    return x
