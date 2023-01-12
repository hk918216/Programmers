def solution(brown, yellow):
    answer = []
    carpet = brown + yellow
    for i in range(1, carpet+1):
        if (carpet / i) % 1 == 0:
            a = carpet / i
            if a >= i:
                if a*2 + i*2 == brown+4:
                    return [a,i]
    return answer
