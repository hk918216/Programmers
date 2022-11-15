def solution(numbers, k):
    answer = 0
    for i in range(k-1):
        numbers.append(numbers.pop(0))
        numbers.append(numbers.pop(0))
    return numbers[0]

def solution(numbers, k):
    answer = 2 * (k - 1) % numbers[-1] + 1
    return answer
