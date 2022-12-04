def solution(common):
    answer = common[1] - common[0]
    if answer == common[2] - common[1]:
        next = common[len(common)-1] + answer
    else:
        a = common[1] // common[0]
        next = common[len(common)-1] * a
    return next
