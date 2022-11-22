#1
def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    for i in range(1, len(my_string),2):
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
    return answer

#2
solution = eval # 매개변수로 받는 식을 문자열로 받아서 실행하는 함수