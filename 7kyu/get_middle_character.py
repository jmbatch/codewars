def get_middle(s):
    count = len(s)
    middle = count // 2
    if count % 2 == 0:
        return s[middle -1 ] + s[middle]
    else:
        return s[middle]
