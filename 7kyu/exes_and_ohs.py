def xo(s):
    s = s.lower()
    count_x = s.count('x')
    count_o = s.count('o')
    if count_x == count_o:
        return True
    else:
        return False
