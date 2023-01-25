from collections import Counter

def solution(k, tangerine):
    answer = 0
    t = Counter(tangerine)
    tt = sorted(list(t.items()), reverse=True, key=lambda x : x[1])
    
    for i,j in tt:
        if k <= 0 :
            break
        k -= j
        answer += 1
    return answer
