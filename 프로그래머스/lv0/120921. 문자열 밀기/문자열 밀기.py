from collections import deque

def solution(A, B):
    # answer = 0
    a,b = deque(A), deque(B)
    for i in range(0, len(a)):
        if a == b:
            return i
        a.rotate(1)
    return -1