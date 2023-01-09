def solution(n):
    answer = n
    a = bin(n).count('1')
    while True:
        answer += 1
        if bin(answer).count('1') == a:
            break
            
    return answer