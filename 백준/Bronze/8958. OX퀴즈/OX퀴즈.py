T = int(input())

for tc in range(1, T + 1):
    ox = input()
    N = len(ox)
    li = [0] * N

    for i in range(N):
        if ox[i] == 'O':
            li[i] += 1
            if ox[i-1] == 'O':
                if i-1 < 0:
                    continue
                li[i] += li[i-1]
        elif ox[i] == 'X':
            continue

    print(sum(li))