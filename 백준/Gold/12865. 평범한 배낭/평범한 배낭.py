import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w = [[0, 0]]
dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

for i in range(n):
    w.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = w[i][0]
        value = w[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])
print(dp[n][k])