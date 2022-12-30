def solution(n, lost, reserve):
    answer = set(lost)
    r = set(reserve)
    lost = list(answer - r)
    reserve = list(r - answer)
    for i in lost:
        answer = i - 1
        r = i + 1
        if answer in reserve:
            reserve.pop(reserve.index(answer))
        elif r in reserve:
            reserve.pop(reserve.index(r))
        else:
            n -= 1
            
    return n
