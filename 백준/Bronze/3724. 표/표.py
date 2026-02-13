import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = float('-inf')
    max_j = 0
    for j in range(M):
        value = 1
        for i in range(N):
            value *= arr[i][j]
        if value >= max_value:
            max_j = j + 1
            max_value = value

    print(max_j)