# 15649 N과 M (1)

def per():
    if len(path) == M:
        print(*path)
        return

    for i in range(1, N+1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        per()
        path.pop()
        used[i] = False

N, M = map(int, input().split())

path = []
used = [False] * (N + 1)
per()