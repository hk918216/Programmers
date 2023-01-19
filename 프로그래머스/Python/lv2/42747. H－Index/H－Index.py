def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in citations:
        if citations.index(i) < i:
            answer += 1
    return answer
