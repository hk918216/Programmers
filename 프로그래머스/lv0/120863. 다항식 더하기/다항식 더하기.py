def solution(polynomial):
    a = polynomial.split(' + ')
    x = 0
    y = 0
    for i in a:
        if 'x' in i and '-' in i and len(i) > 2:
            x += -int(i[1:-1])
        elif 'x' in i and '-' in i and len(i) == 2:
            x -= 1
        elif 'x' in i and len(i) > 1:
            x += int(i[0:-1])
        elif 'x' in i and len(i) == 1:
            x += 1
        else:
            y += int(i)

    answer = ''
    
    if x == 1:
        answer += 'x'
    if x > 1 or x < 0:
        answer += f'{x}x'
    if y != 0 and 'x' in answer:
        answer += f' + {y}'
    if y != 0 and 'x' not in answer:
        answer = f'{y}'
    
    return answer