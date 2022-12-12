def divisor(n):
    a = 0
    for i in range(1, int(n**(1/2)+1)):
        if n % i ==0:
            a += 1
            if i ** 2 != n:
                a += 1
    return a
    
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisor(i) % 2 ==0:
            answer +=i
        else:
            answer -= i
    return answer