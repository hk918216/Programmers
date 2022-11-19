def solution(order):
    answer = 0
    for i in list(str(order)):
        if int(i) == 0 :
            continue
        if int(i)% 3 == 0:
            answer += 1
    return answer