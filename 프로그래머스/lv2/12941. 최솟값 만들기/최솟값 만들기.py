def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    answer = 0

    for i,j in zip(A,B):
        answer += i*j
    return answer