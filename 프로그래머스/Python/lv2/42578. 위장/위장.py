def solution(clothes):
    answer = 1
    dic = {}
    for i,j in clothes:
        dic[j] = dic.get(j,0)+1
    
    for j in dic:
        answer *= (dic[j]+1)
        
    return answer -1
