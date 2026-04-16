def find_set(x):
    if parents[x] == x:
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

    if ref_y > ref_x:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

N = int(input())
M = int(input())
parents = [i for i in range(N + 1)]

net = []
for _ in range(M):
    a, b, c = map(int, input().split())
    net.append((c, a, b))

net.sort()

cost = 0
for c, a, b in net:
    if find_set(a) != find_set(b):
        union(a, b)
        cost += c
    else:
        continue

print(cost)