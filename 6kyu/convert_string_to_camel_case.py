def to_camel_case(text):
    list = [x for x in text]
    if len(list) != 0: 
        for i in range(len(list)):
            if list[i] in ('-', '_'):
                list[i+1] = list[i+1].upper()
    list = ''.join([i for i in list if i not in ('-', '_')])
    return list
