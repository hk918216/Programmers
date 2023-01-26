def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=len)  ## 길이를 중심으로 정렬
    for i in s:
        k = i.split(',')
        for j in k:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
