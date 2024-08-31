def solution(s):
    lst = []
    for letter in s:
        lst.append(letter)
    if (len(lst) % 2) == 0:
        result = [item_1 + item_2 for item_1,
          item_2 in zip(lst[::2], lst[1::2])]
        return result
    else:
        result = lst.append("_")
        result = [item_1 + item_2 for item_1,
          item_2 in zip(lst[::2], lst[1::2])]
        return result
