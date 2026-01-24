def solution(board, moves):
    answer = 0
    stack = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j - 1] == 0:
                continue
            else:
                if len(stack) == 0:
                    stack.append(board[i][j - 1])
                    board[i][j - 1] = 0
                    break
                else:
                    if stack[-1] == board[i][j - 1]:
                        stack.pop()
                        board[i][j - 1] = 0
                        answer += 2
                        break
                    else:
                        stack.append(board[i][j - 1])
                        board[i][j - 1] = 0
                        break
    return answer