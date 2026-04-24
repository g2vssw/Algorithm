N, X = map(int, input().split())
A = list(map(int, input().split()))

li = []
for i in A:
    if i < X:
        li.append(i)

print(*li)