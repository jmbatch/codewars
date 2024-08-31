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
