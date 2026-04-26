N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    n, m = map(int, input().split())
    for i in range(n, n+10):
        for j in range(m, m+10):
            if arr[i][j] == 1:
                continue
            elif arr[i][j] == 0:
                arr[i][j] += 1

result = 0
for li in arr:
    out = li.count(1)
    result += out

print(result)