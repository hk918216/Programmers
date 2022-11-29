def solution(babbling):
    answer = 0
    for i in babbling:
        if 'aya' or 'ye' or 'woo' or 'ma' in i:
            x = i.replace('aya','*').replace('ye','*').replace('woo','*').replace('ma','*')
            x = x.replace("*","")
            if not x:
                answer += 1
    return answer