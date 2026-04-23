from collections import deque

N, K = map(int, input().split())
D = deque()

for num in range(1, N+1):
    D.append(num)

R = deque()
while D:
    for _ in range(K-1):
        D.append(D.popleft())
    R.append(D.popleft())

print("<", end="")
for i in range(N):
    if i < N-1:
        print(R[i], end=', ')
    else:
        print(R[i], end="")
print(">")