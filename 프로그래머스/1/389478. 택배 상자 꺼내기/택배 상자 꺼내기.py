def solution(n, w, num):
    answer = 0
    dj = [1, -1]
    if n % w == 0:
        h = n // w
    else:
        h = n // w + 1
    arr = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 1
    d = 0
    i, j = h - 1, 0
    arr[i][j] = 1
    tj = -1
    while cnt < n:
        if arr[i][j] == num:
            tj = j
        ni, nj = i, j + dj[d]
        if nj < 0 or nj >= w:
            ni, nj = i - 1, j
            d =  (d + 1) % 2
        cnt += 1
        arr[ni][nj] = cnt
        i, j = ni, nj
    for i in range(h):
        if arr[i][tj] == num:
            answer += 1
            break
        if arr[i][tj] != 0:
            answer += 1
    return answer