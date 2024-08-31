def find_it(seq):
    unique_list = []

    for num in seq:
        if num not in unique_list:
            unique_list.append(num)
    for num in unique_list:
        x = seq.count(num)
        if x % 2 != 0:
            return num
