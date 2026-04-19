def recur():
    if len(path) == M:
        re.append(tuple(path[:]))
        return

    for i in range(N):
        path.append(li[i])
        recur()
        path.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

path = []
re = []

recur()

result = list(set(re))
result.sort()

for p in result:
    print(*p)