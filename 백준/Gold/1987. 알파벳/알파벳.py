import sys
input = sys.stdin.readline

def dfs(i, j, cnt):
    global result

    result = max(result, cnt)
    visited[i][j] = 1
    alphabet.add(arr[i][j])

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            continue
        elif visited[ni][nj] == 1 or arr[ni][nj] in alphabet:
            continue
        dfs(ni, nj, cnt + 1)

    visited[i][j] = 0
    alphabet.remove(arr[i][j])

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
alphabet = set()
result = 0

dfs(0, 0, 1)

print(result)