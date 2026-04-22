import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    cheak = list(input().split())
    if len(cheak) == 2:
        queue.append(int(cheak[1]))
    else:
        if cheak[0] == "pop":
            if len(queue) == 0:
                print(-1)
            else:
                value = queue.popleft()
                print(value)
        elif cheak[0] == "size":
            print(len(queue))
        elif cheak[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif cheak[0] == "front":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])