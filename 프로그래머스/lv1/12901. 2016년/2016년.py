def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    answer = (sum(month[:a-1]) + b-1)%7
    return day[answer]