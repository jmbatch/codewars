def square_sum(numbers):
    x = 0
    for i in numbers:
        i = i**2
        x = i + x
    return x
