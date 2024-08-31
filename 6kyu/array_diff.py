def array_diff(a, b):
    d = []
    for i in a:
        if i not in b:
            d.append(i)
    return d
