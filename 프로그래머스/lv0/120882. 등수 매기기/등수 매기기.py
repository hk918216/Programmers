def solution(score):
    answer = []
    x = []
    dict = {}
    for i in range(len(score)):
        answer.append((score[i][0] + score[i][1])/2)
    # reverse = True (내림차순정렬)
    for index, avg in enumerate(sorted(answer,reverse=True), start=1):
        if avg not in dict:
            dict[avg] = index
    for avg in answer:
        x.append(dict[avg])
    return x