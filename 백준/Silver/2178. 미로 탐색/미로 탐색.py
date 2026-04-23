N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
queue = [(0, 0)]

while queue:
    i, j = queue.pop(0)

    if i == N - 1 and j == M - 1:
        break

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        elif arr[ni][nj] == 0:
            continue
        elif arr[ni][nj] == 1:
            arr[ni][nj] = arr[i][j] + 1
            queue.append((ni, nj))

print(arr[N-1][M-1])