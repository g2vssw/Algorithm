N, M = map(int, input().split())
C = int(input())

li_0 = [0, N]
li_1 = [0, M]
for _ in range(C):
    D, K = map(int, input().split())

    if D == 1:
        li_0.append(K)

    else:
        li_1.append(K)

li_0.sort()
li_1.sort()

max_0 = 0
for i in range(len(li_0)-1, 0, -1):
    max_0 = max((li_0[i] - li_0[i - 1]), max_0)

max_1 = 0
for j in range(len(li_1)-1, 0, -1):
    max_1 = max((li_1[j] - li_1[j - 1]), max_1)


result = max_0 * max_1

print(result)