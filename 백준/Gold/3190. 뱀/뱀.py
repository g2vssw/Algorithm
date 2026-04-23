from collections import deque

N = int(input())
arr = [list(0 for _ in range(N)) for _ in range(N)]
a = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for _ in range(a):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 9

L = int(input())

cnt = 0
d = 0
i = 0
j = 0
snake = deque([0, 0])
b_cnt = 0

for _ in range(L):
    X, C = input().split()
    n = int(X)
    b_cnt += 1

    while True:
        arr[i][j] = 1
        if 0 <= i + di[d] < N and 0 <= j + dj[d] < N and arr[i + di[d]][j + dj[d]] == 0:
            arr[i + di[d]][j + dj[d]] = 1
            snake.append(i + di[d])
            snake.append(j + dj[d])
            i, j = i + di[d], j + dj[d]
            arr[snake.popleft()][snake.popleft()] = 0
            cnt += 1

        elif 0 <= i + di[d] < N and 0 <= j + dj[d] < N and arr[i + di[d]][j + dj[d]] == 9:
            arr[i + di[d]][j + dj[d]] = 1
            arr[i + di[d]][j + dj[d]] = 1
            snake.append(i + di[d])
            snake.append(j + dj[d])
            i, j = i + di[d], j + dj[d]
            cnt += 1

        else:
            break

        if b_cnt < L:
            if cnt == n:
                if C == 'D':
                    d = (d + 1) % 4
                    break
                elif C == 'L':
                    d = (d + 3) % 4
                    break
        elif b_cnt == L:
            if cnt == n:
                if C == 'D':
                    d = (d + 1) % 4
                    continue
                elif C == 'L':
                    d = (d + 3) % 4
                    continue

print(cnt+1)