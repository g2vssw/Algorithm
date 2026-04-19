def find_set(x):
    if x == parents[x]:
        return x

    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
route = list(map(int, input().split()))
parents = [i for i in range(N + 1)]

for i in range(N):
    for j in range(i+1, N):
        if arr[i][j] == 1:
            union(i+1, j+1)

flag = 0
for i in range(1, len(route)):
    if find_set(route[0]) != find_set(route[i]):
        flag = 1
        break

if flag:
    print("NO")
else:
    print("YES")