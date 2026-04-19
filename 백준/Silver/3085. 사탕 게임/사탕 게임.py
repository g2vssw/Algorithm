def change(i, j):
    global arr

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
        chk(arr)
        arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]

def chk(arr):
    global result

    for i in range(N):
        S = 'A'
        cnt = 0
        for j in range(N):
            if arr[i][j] != S:
                result = max(result, cnt)
                S = arr[i][j]
                cnt = 0
                cnt += 1
            else:
                cnt += 1

        result = max(result, cnt)

    for j in range(N):
        S = 'A'
        cnt = 0
        for i in range(N):
            if arr[i][j] != S:
                result = max(result, cnt)
                S = arr[i][j]
                cnt = 0
                cnt += 1
            else:
                cnt += 1

        result = max(result, cnt)


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())

arr = [list(input()) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        if result == N:
            break
        change(i, j)

print(result)