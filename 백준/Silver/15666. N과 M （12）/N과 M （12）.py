def recur(start):
    if len(path) == M:
        re.append(tuple(path[:]))
        return

    for i in range(start, N):
        path.append(li[i])
        recur(i)
        path.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

path = []
re = []

recur(0)

result = list(set(re))
result.sort()

for p in result:
    print(*p)