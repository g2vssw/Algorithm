w, l = map(int, input().split())
N = int(input())
end = [tuple(map(int, input().split())) for _ in range(N)]
start = tuple(map(int, input().split()))

total = 0
for i in range(N):
    if start[0] == 1:
        if end[i][0] == 1:
            total += abs(start[1] - end[i][1])
        elif end[i][0] == 2:
            total += min(start[1] + end[i][1], w * 2 - end[i][1] - start[1]) + l
        elif end[i][0] == 3:
            total += end[i][1] + start[1]
        elif end[i][0] == 4:
            total += end[i][1] + w - start[1]

    elif start[0] == 2:
        if end[i][0] == 1:
            total += min(start[1] + end[i][1], w * 2 - end[i][1] - start[1]) + l
        elif end[i][0] == 2:
            total += abs(start[1] - end[i][1])
        elif end[i][0] == 3:
            total += l - end[i][1] + start[1]
        elif end[i][0] == 4:
            total += l - end[i][1] + w - start[1]

    elif start[0] == 3:
        if end[i][0] == 1:
            total += end[i][1] + start[1]
        elif end[i][0] == 2:
            total += l - start[1] + end[i][1]
        elif end[i][0] == 3:
            total += abs(start[1] - end[i][1])
        elif end[i][0] == 4:
            total += min(start[1] + end[i][1], l * 2 - end[i][1] - start[1]) + w

    elif start[0] == 4:
        if end[i][0] == 1:
            total += w - end[i][1] + start[1]
        elif end[i][0] == 2:
            total += w - end[i][1] + start[1]
        elif end[i][0] == 3:
            total += min(start[1] + end[i][1], l * 2 - end[i][1] - start[1]) + w
        elif end[i][0] == 4:
            total += abs(start[1] - end[i][1])

print(total)