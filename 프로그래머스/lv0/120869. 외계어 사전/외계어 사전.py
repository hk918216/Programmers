def solution(spell, dic):
    answer = set(spell)
    for i in dic:
        if answer.issubset(set(i)):
            return 1
    return 2