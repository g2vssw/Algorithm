def recur():
    if len(path) == M:
        print(*path)
        return

    for i in li:
        if used[i]:
            continue

        used[i] = True
        path.append(i)
        recur()
        path.pop()
        used[i] = False


N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

path = []
used = [False] * (li[-1] + 1)
recur()