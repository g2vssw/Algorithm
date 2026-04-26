H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
answer = []

for i in range(H):
    de = -1
    result = []
    for j in range(W):
        if arr[i][j] == 'c':
            de = 0
        else:
            if de != -1:
                de += 1

        result.append(de)

    answer.append(result)

for i in answer:
    print(*i)