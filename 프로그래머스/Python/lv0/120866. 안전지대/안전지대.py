def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for a in range(i-1, i+2):
                    if a == -1 or a == n:
                        continue
                    for b in range(j-1, j+2):
                        if b == -1 or b == n:
                            continue
                        if board[a][b] != 1:
                            board[a][b] = 2
    for i in range(n):
        answer += board[i].count(0)
    return answer
