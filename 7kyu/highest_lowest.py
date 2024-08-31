def high_and_low(numbers):
    arr = sorted(numbers.split(), key=int)
    return '{} {}'.format(arr[-1], arr[0])
