def solution(n, arr1, arr2):
    answer = []
    m = []
    for i in range(len(arr1)):
        c = format(arr1[i]|arr2[i], 'b').zfill(n)
        answer.append(c)
        if answer[i][i] == 0:
            answer.replace()
    for i in answer:
        k = i.replace('1','#')
        k = k.replace('0',' ')
        m.append(k)
    return m
