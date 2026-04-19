import sys
input = sys.stdin.readline

def recur():
    if len(path) == M:
        re.append(tuple(path[:]))
        return

    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        path.append(li[i])
        recur()
        path.pop()
        used[i] = False

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

path = []
re = []
used = [False] * N

recur()

result = list(set(re))
result.sort()

for p in result:
    print(*p)