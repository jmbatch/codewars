def solution(string, ending):
    endlength = len(ending)
    if endlength == 0:
        return True
    if string[-endlength:] == ending:
        return True
    else:
        return False
