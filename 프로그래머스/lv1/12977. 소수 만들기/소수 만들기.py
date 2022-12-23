from itertools import combinations

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    nums = list(combinations(nums,3))
    for i in nums:
        if isPrime(sum((i))) == True:
            answer += 1
            
    return answer