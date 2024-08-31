# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'


def solution(string):
    # slice string [startIndex:endIndex:step] (-1 goes backwards)
    return string[::-1]
