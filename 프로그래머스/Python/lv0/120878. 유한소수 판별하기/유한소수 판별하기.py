import math

def solution(a, b):
    b = b/math.gcd(a,b)
    while b != 1:
        if b % 2 == 0:
            b = b//2
        elif b % 5 == 0:
            b = b//5
        else:
            return 2
    return 1

# def solution(a,b):
#     return 1 if a/b * 1000 % 1 == 0 else 2
