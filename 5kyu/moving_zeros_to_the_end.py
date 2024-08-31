def move_zeros(lst):
    count = lst.count(0)
    for i in range(count):
        lst.remove(0)
    for i in range(count):
        lst.append(0)
    return lst
