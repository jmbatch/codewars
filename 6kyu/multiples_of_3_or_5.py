def solution(n):
    multiples = []
    num_list = [i for i in range(3, n)]
    if n > 0:
        for i in num_list:
            if i % 3 == 0 or i % 5 == 0:
                multiples.append(i)
            else:
                pass
        return sum(multiples)
    else:
        return 0
