import sys
input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:
        return x

    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(x, y):
    global flag
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        flag = 1
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

n, m = map(int, input().split())
parents = [i for i in range(n)]
flag = 0

for i in range(1, m + 1):
    a, b = map(int, input().split())

    union(a, b)

    if flag:
        print(i)
        break

if not flag:
    print(0)