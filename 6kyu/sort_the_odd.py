def sort_array(source_array):
    odd = []
    for num in source_array:
        if (int(num) % 2) != 0:
            odd.append(num)
            odd.sort()
    for i in range(0, len(source_array)):
        if (source_array[i] % 2) != 0:
            popped = odd.pop(0)
            source_array[i] = popped
    return source_array
