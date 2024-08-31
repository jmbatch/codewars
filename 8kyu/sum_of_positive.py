# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    neg_num = [num for num in arr if num < 0]
    if len(neg_num) == len(arr):
        return 0
    else:
        for i in arr[:]:
            if i <= 0:
                neg = arr.index(i)
                arr.pop(neg)
    return sum(arr)
