def per(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N+1):
        if used[i]:
            continue
        elif len(path) != 0 and path[-1] > i:
            continue
        used[i] = True
        path.append(i)
        per(start + 1)
        path.pop()
        used[i] = False

N, M = map(int, input().split())

path = []
used = [False] * (N + 1)
per(1)