def rotation(gears, inx, direction):
    gear = gears[inx]
    if direction == 1:
        gear[0], gear[1], gear[2], gear[3], gear[4], gear[5], gear[6], gear[7] = \
            gear[7], gear[0], gear[1], gear[2], gear[3], gear[4], gear[5], gear[6]
    elif direction == -1:
        gear[0], gear[1], gear[2], gear[3], gear[4], gear[5], gear[6], gear[7] = \
            gear[1], gear[2], gear[3], gear[4], gear[5], gear[6], gear[7], gear[0]

    return gears

gears = [list(input()) for _ in range(4)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())
    i = n - 1

    if i+1 < 4 and gears[i][2] != gears[i+1][6]:
        if i+2 < 4 and gears[i+1][2] != gears[i+2][6]:
            if i+3 < 4 and gears[i+2][2] != gears[i+3][6]:
                gears = rotation(gears, i+3, -d)
                gears = rotation(gears, i+2, d)
                gears = rotation(gears, i+1, -d)
            else:
                gears = rotation(gears, i+2, d)
                gears = rotation(gears, i+1, -d)
        else:
            gears = rotation(gears, i+1, -d)

    if i-1 >= 0 and gears[i][6] != gears[i-1][2]:
        if i-2 >= 0 and gears[i-1][6] != gears[i-2][2]:
            if i-3 >= 0 and gears[i-2][6] != gears[i-3][2]:
                gears = rotation(gears, i-3, -d)
                gears = rotation(gears, i-2, d)
                gears = rotation(gears, i-1, -d)
            else:
                gears = rotation(gears, i-2, d)
                gears = rotation(gears, i-1, -d)
        else:
            gears = rotation(gears, i-1, -d)

    gears = rotation(gears, i, d)


result = []
for i in range(4):
    result.append(int(gears[i][0]))

cnt = 0
for i in range(4):
    cnt += result[i] * 2 ** i

print(cnt)