def solution(n):
    answer = []
    a=[]
    for i in range(2,n+1):  
        if n%i ==0:
            a.append(i)    

    for i in a: 
        for j in range(2,10000):
            if i*j in a:
                a.remove(i*j)
    a.sort()
    return a