N = int(input())
arr = [list(input()) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
max_cnt = 0
V = [[0] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        A = arr[y][x]
        V[y][x] = 1

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < N and arr[y][x] != arr[ny][nx] and V[ny][nx] == 0:
                arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]

                for l in range(N):
                    w_cnt = 1
                    for r in range(N - 1):
                        if arr[l][r] == arr[l][r + 1]:
                            w_cnt += 1
                        elif arr[l][r] != arr[l][r + 1]:
                            max_cnt = max(max_cnt, w_cnt)
                            w_cnt = 1
                    max_cnt = max(max_cnt, w_cnt)

                    if max_cnt == N:
                        break

                for l in range(N):
                    h_cnt = 1
                    for r in range(N - 1):
                        if arr[r][l] == arr[r + 1][l]:
                            h_cnt += 1
                        elif arr[r][l] != arr[r + 1][l]:
                            max_cnt = max(max_cnt, h_cnt)
                            h_cnt = 1
                    max_cnt = max(max_cnt, h_cnt)

                    if max_cnt == N:
                        break

                arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]
print(max_cnt)