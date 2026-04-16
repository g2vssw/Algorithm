def dfs(node):
    global cnt
    if not graph[node]:
        cnt += 1
        return

    for next_node in graph[node]:
        dfs(next_node)

N = int(input())
li = list(map(int, input().split()))
T = int(input())
graph = [[] for _ in range(N)]
cnt = 0

start = 0
for i in range(N):
    if li[i] == -1:
        start = i
        if i == T:
            graph[i] = []
            break
        continue
    graph[li[i]].append(i)

for node in graph:
    if T in node:
        node.remove(T)

if T == start:
    print(cnt)
else:
    dfs(start)
    print(cnt)