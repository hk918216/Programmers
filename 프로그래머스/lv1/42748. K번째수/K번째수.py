def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[int(commands[i][0]-1):int(commands[i][1])]
        arr = sorted(arr)
        k = arr[int(commands[i][2]-1)]
        answer.append(k)
    return answer