import re

def solution(my_string):
    return sorted(map(int,list(re.sub('[^0-9]',"", my_string))))

def solution(my_string):
    return sorted([int(s) for s in my_string if s.isdigit()])
