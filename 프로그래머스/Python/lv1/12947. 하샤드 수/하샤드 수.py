def solution(x):
    answer = True
    a = str(x)
    b = 0
    for i in a:
        b += int(i)
    if x % b == 0:
        return answer
    else:
        return False
