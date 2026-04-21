def per():
    if len(path) == M:
        print(*path)
        return

    for i in range(1, N+1):

        path.append(i)
        per()
        path.pop()

N, M = map(int, input().split())

path = []
per()