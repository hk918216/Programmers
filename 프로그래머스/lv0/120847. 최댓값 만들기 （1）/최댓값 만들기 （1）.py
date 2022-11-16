def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]

def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
