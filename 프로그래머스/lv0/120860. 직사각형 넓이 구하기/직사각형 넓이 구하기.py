def solution(dots):
    for i in range(1,4):
        if dots[i][0] == dots[0][0]:
            w = abs(dots[i][1] - dots[0][1])
        if dots[i][1] == dots[0][1]:
            h = abs(dots[i][0] - dots[0][0])
    return w * h