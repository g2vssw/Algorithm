di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N = int(input())
T = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
num = N*N
k = 0
i, j = 0, 0

while num > 0:
    arr[i][j] = num

    if num == T:
        re_i, re_j = i + 1, j + 1

    n_i, n_j = i + di[k], j + dj[k]

    if n_i < 0 or n_i >= N or n_j < 0 or n_j >= N or arr[n_i][n_j] != 0:
        k = (k + 1) % 4

    n_i, n_j = i + di[k], j + dj[k]

    i = n_i
    j = n_j
    num -= 1

for re in arr:
    print(*re)
print(re_i, re_j)