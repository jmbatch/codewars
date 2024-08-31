def find_even_index(arr):
    even_index = []
    for i in range(0, len(arr)):
        right_list = arr[i + 1:]
        left_list = arr[0:i]
        right_total = 0
        left_total = 0
        for x in range(0, len(right_list)):
            right_total = right_total + right_list[x]
        for x in range(0, len(left_list)):
            left_total = left_total + left_list[x]
        if left_total == right_total:
            even_index.append(i)
    if len(even_index) == 0:
        return -1
    else:
        even_index.sort()
        return even_index[0]
