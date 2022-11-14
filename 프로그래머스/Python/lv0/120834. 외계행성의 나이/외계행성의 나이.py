def solution(age):
    list = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''
    for i in str(age):
        answer += list[int(i)]
    return answer

def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(int(i)+97)
    return answer
