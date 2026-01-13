def solution(board):
    answer = 0
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni < 0 or ni >= n or nj < 0 or nj >= n:
                        continue
                    if board[ni][nj] == 0:
                        board[ni][nj] = 2
    for li in board:
        answer += li.count(0)
    return answer