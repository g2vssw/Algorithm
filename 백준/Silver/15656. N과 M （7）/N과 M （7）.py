def recur():
    if len(path) == M:
        print(*path)
        return

    for i in range(N):

        path.append(li[i])
        recur()
        path.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

path = []
recur()