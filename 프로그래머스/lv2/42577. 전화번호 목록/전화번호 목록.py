def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        if phone_book[i+1].startswith(a):
            answer = False
            return answer
    return answer