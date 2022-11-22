def solution(quiz):
    answer = []
    for i in quiz:
        f = i.split('=')
        for j in range(len(f)):
            if eval(f[0]) == eval(f[1]):
                answer.append('O')
                break
            else:
                answer.append('X')
                break
    return answer