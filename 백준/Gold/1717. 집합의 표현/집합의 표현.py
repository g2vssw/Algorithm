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

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

for _ in range(m):
    p, a, b = map(int, input().split())

    if p == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")