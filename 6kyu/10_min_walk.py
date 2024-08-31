def is_valid_walk(walk):
    northsouth = 0
    eastwest = 0
    if len(walk) == 10:
        for i in walk:
            if i == 'e':
                eastwest = eastwest + 1
            if i == 'w':
                eastwest = eastwest - 1
            if i == 'n':
                northsouth = northsouth + 1
            if i == 's':
                northsouth = northsouth - 1
        if eastwest == 0 and northsouth == 0:
            return True
        else:
            return False
    else:
        return False
