def solution(s):
    answer = ''
    a = s.split(' ')
    
    for i in range(len(a)):
        a[i] = a[i].capitalize()
        
    answer = ' '.join(a)
    return answer