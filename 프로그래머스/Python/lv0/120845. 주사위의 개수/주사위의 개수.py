def solution(box, n):
    answer = 1
    for i in range(len(box)):
        answer *= box[i]//n
    return answer

def solution(box, n):
    answer = (box[0]//n) * (box[1]//n) * (box[2]//n)
    return answer
