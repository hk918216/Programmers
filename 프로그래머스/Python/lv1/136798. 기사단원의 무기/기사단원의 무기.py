def divisor(n):
    a = 0
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            a += 1
            if i**2 != n:
                a += 1
    return a

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        if divisor(i) > limit:
            answer += power
        else: 
            answer += divisor(i)
    return answer
