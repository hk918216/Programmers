def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort()
        if len(rank) > k:
            del rank[0]
        answer.append(rank[0])
    return answer