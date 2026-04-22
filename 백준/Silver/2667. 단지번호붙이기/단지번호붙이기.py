def bfs(i, j):
    global cnt
    global apt

    if visited[i][j] == 1 or arr[i][j] == 0:
        return
    elif visited[i][j] == 0:
        visited[i][j] = 1
        apt += 1
        cnt += 1

    queue = [(i, j)]

    while queue:
        i, j = queue.pop()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            elif arr[ni][nj] == 0 or visited[ni][nj] == 1:
                continue
            visited[ni][nj] = 1
            queue.append((ni, nj))
            apt += 1


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cnt = 0
apt = 0
apt_list = []

for i in range(N):
    for j in range(N):
        bfs(i, j)
        if apt > 0:
            apt_list.append(apt)
            apt = 0

apt_list.sort()

print(cnt)
for r in apt_list:
    print(r)