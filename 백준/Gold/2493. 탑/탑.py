import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
li = list(map(int, input().split()))

q = deque()
result = deque()

for i in range(N):
    while True:
        if not q:
            q.append((li[i], i))
            result.append(0)
            break
        else:
            if q[-1][0] < li[i]:
                q.pop()
                if not q:
                    q.append((li[i], i))
                    result.append(0)
                    break
            else:
                result.append(q[-1][1] + 1)
                q.append((li[i], i))
                break
print(*result)