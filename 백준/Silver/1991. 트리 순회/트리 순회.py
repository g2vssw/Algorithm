def dfs(node):
    if node == -19:
        return

    left = graph[node][0]
    right = graph[node][1]

    preorder.append(chr(node + 65))
    dfs(left)
    inorder.append(chr(node + 65))
    dfs(right)
    postorder.append(chr(node + 65))

N = int(input())
graph = [[] for _ in range(N)]

preorder = []
inorder = []
postorder = []
for _ in range(N):
    q, w, e = map(ord, input().split())
    q, w, e = q - 65, w - 65, e - 65
    graph[q].append(w)
    graph[q].append(e)

dfs(0)

print("".join(preorder))
print("".join(inorder))
print("".join(postorder))