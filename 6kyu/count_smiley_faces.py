def count_smileys(arr):
    face = 0
    for i in arr:
        if i.find(':') != -1 or i.find(';') != -1:
            if i.find('D') != -1 or i.find(')') != -1:
                if i.find('o') == -1:
                    face = face + 1
                else:
                    pass
        else:
            pass
    print(arr)
    return face
