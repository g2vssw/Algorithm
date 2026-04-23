from collections import deque

N = int(input())
D = deque()

for num in range(N, 0, -1):
    D.append(num)

while D:
    if len(D) != 1:
        D.pop()
        D.appendleft(D.pop())
    elif len(D) == 1:
        print(*D)
        break