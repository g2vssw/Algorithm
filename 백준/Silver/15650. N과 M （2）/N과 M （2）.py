def per(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N+1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        per(i)
        path.pop()
        used[i] = False

N, M = map(int, input().split())

path = []
used = [False] * (N + 1)
per(1)