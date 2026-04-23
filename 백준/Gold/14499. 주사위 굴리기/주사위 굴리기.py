def move(order_num, dice):
    if order_num == 1:  # 1
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif order_num == 2:  # 2
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif order_num == 3:  # 3
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    elif order_num == 4:  # 4
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

    return dice

N, M, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0] * 7
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

for order_num in order:
    n_x = x + di[order_num-1]
    n_y = y + dj[order_num-1]
    if n_x < 0 or n_x >= N or n_y < 0 or n_y >= M:
        continue
    dice = move(order_num, dice)
    x, y = n_x, n_y
    print(dice[1])
    if arr[x][y] == 0:
        arr[x][y] = dice[6]
    elif arr[x][y] != 0:
        dice[6] = arr[x][y]
        arr[x][y] = 0