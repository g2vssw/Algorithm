def solution(keyinput, board):
    answer = []
    s_i = 0
    s_j = 0
    for s in keyinput:
        if s == "left":
            if s_i - 1 < -(board[0] / 2):
                continue
            s_i -= 1
        elif s == "right":
            if s_i + 1 > board[0] / 2:
                continue
            s_i += 1
        elif s == "up":
            if s_j + 1 > board[1] / 2:
                continue
            s_j += 1
        else:
            if s_j - 1 < -(board[1] / 2):
                continue
            s_j -= 1
    answer.append(s_i)
    answer.append(s_j)
    return answer