import sys
input = sys.stdin.readline

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
        count[ref_x] += count[ref_y]
    else:
        parents[ref_x] = ref_y
        count[ref_y] += count[ref_x]

T = int(input())

for _ in range(T):
    F = int(input())

    parents = []
    count = []
    people = {}
    idx = 0
    for _ in range(F):
        p1, p2 = map(str, input().split())
        if p1 not in people:
            people[p1] = idx
            parents.append(idx)
            count.append(1)
            idx += 1
        if p2 not in people:
            people[p2] = idx
            parents.append(idx)
            count.append(1)
            idx += 1

        union(people[p1], people[p2])

        print(count[find_set(people[p1])])