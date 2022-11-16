import math

def solution(n):
    array = []
    for i in range(1,11):
        array.append(math.factorial(i))
        
    for j in range(len(array)):
        if n == array[j]:
            return j+1
        elif n > array[j] and n < array[j+1]:
            return j+1
        
def solution(n):
    k = 10
    while n < math.factorial(k):
        k -= 1
    return k    
