def solution(s):
    answer = 0
    a = 0
    b = 0
    for i in s:
        if a == b:
            answer += 1
            j = i
        if j == i:
            a += 1
        else:
            b += 1
    return answer
