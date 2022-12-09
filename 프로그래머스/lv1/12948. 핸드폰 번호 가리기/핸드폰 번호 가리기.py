def solution(phone_number):
    a = phone_number
    
    return a.replace(a[:-4],'*'*len(a[:-4]))