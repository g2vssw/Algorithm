def solution(park, routes):
    h = len(park)
    w = len(park[0])
    si, sj = 0, 0
    flag = 0
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                si, sj = i, j
                flag = 1
                break
        if flag:
            break
    for dc in routes:
        d, c = dc.split()
        cheak = 1
        for k in range(1, int(c) + 1):
            if d == "N":
                ni, nj = si - k, sj
            elif d == "S":
                ni, nj = si + k, sj
            elif d == "W":
                ni, nj = si, sj - k
            else:
                ni, nj = si, sj + k
            if ni < 0 or ni >= h or nj < 0 or nj >= w or park[ni][nj] == "X":
                cheak = 0
                break
        if cheak:
            if d == "N":
                si, sj = si - int(c), sj
            elif d == "S":
                si, sj = si + int(c), sj
            elif d == "W":
                si, sj = si, sj - int(c)
            else:
                si, sj = si, sj + int(c)
    answer = [si, sj] 
    return answer