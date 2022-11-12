from collections import Counter

def solution(array):
    a = Counter(array)
    m = a.most_common()
    mode = m[0][1]
    modes = []
    for i in m:
        if i[1] == mode:
            modes.append(i[0])
    if len(modes) >=2:
        return -1
    else:
        return modes[0]
    
