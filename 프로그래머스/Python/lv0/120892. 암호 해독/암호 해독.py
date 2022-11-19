def solution(cipher, code):
    
    return cipher[code-1::code]

def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
        if (i+1) % code == 0:
            answer += cipher[i]
    return answer
