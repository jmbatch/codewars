# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# my solution
def accum(s):
    n = 0
    lst = []
    for letter in s:
        lst.append(letter)
    for letter in lst:
        lst[n] = lst[n] * (n + 1)
        n += 1
    lst = '-'.join(lst)
    return lst.title()
