N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
direction = d
cnt = 0

i, j = r, c
while True:
    if arr[i][j] == 0:
        arr[i][j] = 2
        cnt += 1

    move = False
    for k in range(4):
        n_i = i + di[k]
        n_j = j + dj[k]

        if arr[n_i][n_j] == 0:
            move = True
            break
            
    while move:
        direction = (direction+3) % 4
        if arr[i+di[direction]][j+dj[direction]] == 0:
            i = i+di[direction]
            j = j+dj[direction]
            break

    if not move:
        if arr[i-di[direction]][j-dj[direction]] != 1:
            i = i - di[direction]
            j = j - dj[direction]
        elif arr[i-di[direction]][j-dj[direction]] == 1:
            break

print(cnt)