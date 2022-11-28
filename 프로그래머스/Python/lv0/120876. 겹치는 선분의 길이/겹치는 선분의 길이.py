#1
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

#2
def solution(lines):
    sets = [set(range(min(i), max(i))) for i in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
