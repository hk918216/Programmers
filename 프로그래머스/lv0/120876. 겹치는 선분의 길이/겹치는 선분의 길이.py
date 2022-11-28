def solution(lines):
    answer = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        x,y = line
        for i in range(x,y):
            answer[i + 100].add(index)
            
    count= 0 
    for line in answer :
        if len(line) > 1:
            count += 1
    return count