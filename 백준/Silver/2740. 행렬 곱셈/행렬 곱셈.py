import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    column = []
    for j in range(K):
        value = 0
        for k in range(M):
            value += matrix1[i][k] * matrix2[k][j]
        column.append(value)
    result = " ".join(map(str, column))

    print(result)