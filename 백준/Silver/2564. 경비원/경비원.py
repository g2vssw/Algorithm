import copy

def bfs(start, q, arr):

    queue = [start]
    while queue:
        i, j = queue.pop(0)

        if (i, j) == end[q]:
            return arr[i][j] - 1

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni >= l+1 or nj < 0 or nj >= w+1:
                continue
            elif arr[ni][nj] == 0:
                continue
            elif arr[ni][nj] == 1:
                arr[ni][nj] = arr[i][j] + 1
                queue.append((ni, nj))

def trans(x, y):
    if x == 1:
        x = 0
        y = y
        return x, y
    elif x == 2:
        x = l
        y = y
        return x, y
    elif x == 3:
        x = y
        y = 0
        return x, y
    elif x == 4:
        x = y
        y = w
        return x, y

w, l = map(int, input().split())
N = int(input())
end = []
for _ in range(N):
    x, y = map(int, input().split())
    end.append(trans(x, y))
x, y = tuple(map(int, input().split()))
start = trans(x, y)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

arr = [list(0 for _ in range(w+1)) for _ in range(l+1)]

for i in range(w+1):
    arr[0][i] = 1
    arr[-1][i] = 1
for j in range(l+1):
    arr[j][0] = 1
    arr[j][-1] = 1

result = 0
for q in range(N):
    arr2 = copy.deepcopy(arr)
    value = bfs(start, q, arr2)

    if value is not None:  # None이 아닐 때만 더하기
        result += value

print(result)