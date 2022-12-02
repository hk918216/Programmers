from collections import Counter

def solution(before, after):
    # answer = 0
    before = Counter(before)
    after = Counter(after)
    if before == after :
        return 1
    else:
        return 0
