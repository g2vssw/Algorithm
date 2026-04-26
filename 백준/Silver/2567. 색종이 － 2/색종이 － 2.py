N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

for _ in range(N):
    n, m = map(int, input().split())
    for i in range(n, n+10):
        for j in range(m, m+10):
            if arr[i][j] == 1:
                continue
            elif arr[i][j] == 0:
                arr[i][j] += 1

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            if i-1 < 0:
                cnt += 1
            elif arr[i-1][j] == 0:
                cnt += 1
            elif i+1 >= 100:
                cnt += 1
            elif arr[i+1][j] == 0:
                cnt += 1

for j in range(100):
    for i in range(100):
        if arr[i][j] == 1:
            if j-1 < 0:
                cnt += 1
            elif arr[i][j-1] == 0:
                cnt += 1
            elif j+1 >= 100:
                cnt += 1
            elif arr[i][j+1] == 0:
                cnt += 1

print(cnt)