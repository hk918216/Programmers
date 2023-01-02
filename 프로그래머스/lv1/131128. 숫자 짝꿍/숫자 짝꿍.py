def solution(X, Y):
    answer = []
    xdic = dict()
    ydic = dict()
    
    for i in X:
        xdic[i] = xdic.get(i,0)+1
    for j in Y:
        ydic[j] = ydic.get(j,0)+1
    
    for k,v in xdic.items():
        if k in ydic.keys():
            while ydic[k]>0  and xdic[k]>0:
                answer.append(k)
                xdic[k]=xdic.get(k)-1
                ydic[k]=ydic.get(k)-1
    
    if (len(answer)==0):
        return '-1'
    if (answer.count('0')==len(answer)):
        return '0'
    answer.sort(reverse=True)
    return ''.join(answer)