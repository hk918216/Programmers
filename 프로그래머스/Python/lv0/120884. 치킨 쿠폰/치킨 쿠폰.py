def solution(chicken):
    # answer = -1
    count = 0
    while chicken >= 10:
        b = chicken // 10
        count += b
        chicken = chicken%10+b
    return count
