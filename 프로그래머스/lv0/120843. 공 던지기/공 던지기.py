def solution(numbers, k):
    answer = 0
    for i in range(k-1):
        numbers.append(numbers.pop(0))
        numbers.append(numbers.pop(0))
    return numbers[0]