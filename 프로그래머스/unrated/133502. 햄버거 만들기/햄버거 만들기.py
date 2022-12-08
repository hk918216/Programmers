def solution(ingredient):
    answer = 0
    a = []
    for i in ingredient:
        a.append(i)
        if a[-4:] == [1,2,3,1]:
            answer += 1
            del a[-4:]
    return answer