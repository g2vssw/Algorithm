import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    global cnt

    if arr[i][j] != 0:
        visited[i][j] = 0
        return
    elif arr[i][j] == 0 and visited[i][j] == 0:
        visited[i][j] = 1
        cnt += 1


    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        if ni < 0 or ni >= M or nj < 0 or nj >= N:
            continue
        elif arr[ni][nj] != 0 and visited[ni][nj] != 0:
            continue
        elif arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            cnt += 1
            dfs(ni, nj)


M, N, K = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

cnt = 0
result = []
for i in range(M):
    for j in range(N):
        dfs(i, j)
        if cnt > 0:
            result.append(cnt)
            cnt = 0
        else:
            continue

result.sort()

print(len(result))
print(*result)