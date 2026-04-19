N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

result = 21e8
for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if arr[k][l] == "W":
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if arr[k][l] == "B":
                        cnt1 += 1
                    else:
                        cnt2 += 1

        result = min(result, cnt1, cnt2)

print(result)