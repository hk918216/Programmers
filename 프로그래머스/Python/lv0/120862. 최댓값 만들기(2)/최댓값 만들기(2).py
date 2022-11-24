def solution(numbers):
    answer = sorted(numbers)
    return max(answer[0]*answer[1] , answer[-1]*answer[-2])
