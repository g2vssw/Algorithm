def bingo(arr):
    chk = 0
    for i in range(5):
        if sum(arr[i]) == 0:
            chk += 1
        else:
            continue

    length = list(zip(*arr))
    for i in range(5):
        if sum(length[i]) == 0:
            chk += 1
        else:
            continue

    cross1 = 0
    cross2 = 0
    for i in range(5):
        cross1 += arr[i][i]
        cross2 += arr[i][5-i-1]

    if cross1 == 0:
        chk += 1
    if cross2 == 0:
        chk += 1

    if chk >= 3:
        return True
    else:
        return False

arr = [list(map(int, input().split())) for _ in range(5)]
li = []
for _ in range(5):
    li = li + list(map(int, input().split()))

cnt = 0
for k in range(25):
    for i in range(5):
        for j in range(5):
            if li[k] == arr[i][j]:
                arr[i][j] = 0
                cnt += 1
                break

    if cnt >= 12:
        check = bingo(arr)
        if check:
            break
        else:
            continue

print(cnt)