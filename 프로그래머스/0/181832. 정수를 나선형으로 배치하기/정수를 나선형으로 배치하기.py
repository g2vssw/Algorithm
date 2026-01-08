def solution(n):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    answer = [[0 for _ in range(n)] for _ in range(n)]

    i, j = 0, 0
    answer[i][j] = 1
    
    if n == 1:
        return answer
    
    cnt = 1
    dr = 1
    while True:
        if cnt == n * n:
            break
        
        if i + di[dr] < 0 or i + di[dr] >= n or j + dj[dr] < 0 or j + dj[dr] >= n:
            dr = (dr + 1) % 4
            continue
        elif answer[i + di[dr]][j + dj[dr]] != 0:
            dr = (dr + 1) % 4
            continue
        answer[i + di[dr]][j + dj[dr]] = answer[i][j] + 1
        i, j = i + di[dr], j + dj[dr]
        cnt += 1
    
    return answer