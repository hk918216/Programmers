def solution(sides):
    answer = 0
    a,b = sides[0], sides[1]
    for i in range(1, a+b+1):
        if (a+b+i) > 2*max(a,b,i):
            answer += 1
    return answer

def solution(sides):
    return sum(sides) - max(sides) + min(sides) -1