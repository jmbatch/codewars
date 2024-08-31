def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        frnds = names[0]
        return f'{frnds} likes this'
    if len(names) == 2:
        frnds, frnds2 = names[0], names[1]
        return f'{frnds} and {frnds2} like this'
    if len(names) == 3:
        frnds1, frnds2, frnds3 = names[0], names[1], names[2]
        return f'{frnds1}, {frnds2} and {frnds3} like this'
    if len(names) >= 4:
        frnds, frnds2 = names[0], names[1]
        lngth = len(names) - 2
        return f'{frnds}, {frnds2} and {lngth} others like this'
