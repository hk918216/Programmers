def solution(age):
    list = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''
    for i in str(age):
        answer += list[int(i)]
    return answer

