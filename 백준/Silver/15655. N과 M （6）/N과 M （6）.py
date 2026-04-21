def recur(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N):
        if used[i]:
            continue

        used[i] = True
        path.append(li[i])
        recur(i)
        path.pop()
        used[i] = False

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

path = []
used = [False] * N
recur(0)