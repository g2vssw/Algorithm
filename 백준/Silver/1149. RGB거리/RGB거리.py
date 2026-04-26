import sys

input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)] # 0으로 초기화
dp[0] = rgb[0]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0] # 삘간색 0
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1] # 초록색 1
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2] # 파란색 2

print(min(dp[-1]))