def recur(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N):

        path.append(li[i])
        recur(i)
        path.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

path = []
recur(0)