from collections import deque

N = int(input())
D = deque()

for num in range(N, 0, -1):
    D.append(num)

result = deque()
while D:
    result.append(D.pop())
    if len(D) != 0:
        D.appendleft(D.pop())

print(*result)