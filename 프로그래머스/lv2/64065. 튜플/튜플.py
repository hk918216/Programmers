def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=len)
    for i in s:
        k = i.split(',')
        for j in k:
            if int(j) not in answer:
                answer.append(int(j))
    return answer