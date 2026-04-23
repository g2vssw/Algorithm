from collections import deque

N, M = map(int, input().split())
li = deque(map(int, input().split()))
D = deque()

for i in range(1, N+1):
    D.append(i)

cnt = 0
while li:
    if li[0] == D[0]:
            li.popleft()
            D.popleft()
    else:
        if len(D) / 2 < D.index(li[0]):
            D.rotate(1)
            cnt += 1
        else:
            D.rotate(-1)
            cnt += 1

print(cnt)