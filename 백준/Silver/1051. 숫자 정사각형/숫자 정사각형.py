N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

max_k = 1
for i in range(N):
    for j in range(M):
        cheak = arr[i][j]
        V = min((N - i), (M - j))
        for k in range(1, V):
            if cheak == arr[i + k][j + k] and cheak == arr[i + k][j] and cheak == arr[i][j + k]:
                max_k = max(max_k, (k + 1) ** 2)

print(max_k)