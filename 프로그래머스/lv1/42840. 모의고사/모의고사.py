def solution(answers):
    answer = []
    score = [0,0,0]
    o = [1,2,3,4,5]
    w = [2,1,2,3,2,4,2,5]
    t = [3,3,1,1,2,2,4,4,5,5]
    for i, j in enumerate(answers):
        if j == o[i%len(o)]:
            score[0] += 1
        if j == w[i%len(w)]:
            score[1] += 1
        if j == t[i%len(t)]:
            score[2] += 1
    a = max(score)
    for i in range(3):
        if a == score[i]:
            answer.append(i+1)
    return answer