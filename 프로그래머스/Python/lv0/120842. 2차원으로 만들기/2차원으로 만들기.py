def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        answer.append(num_list[i*n:i*n+n])
        
    return answer

#2
import numpy as np

def solution(num_list, n):
    list = np.array(num_list).reshape(-1, n)
    return list.tolist()   

# tolist() : array를 list로 변경
# array 차원 그대로 유지
