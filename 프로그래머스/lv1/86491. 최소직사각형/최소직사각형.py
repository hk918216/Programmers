def solution(sizes):
    answer = []
    m = []
    for i in range(len(sizes)):
        answer.append(max(sizes[i]))
        m.append(min(sizes[i]))
    
    return max(answer)*max(m)