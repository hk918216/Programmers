#1
def solution(my_string, overwrite_string, s):
    return my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]
    
#2
def solution(my_string, overwrite_string, s):
    answer = ''
    answer += my_string[:s]
    answer += overwrite_string
    answer += my_string[s+len(overwrite_string):]
    return answer
