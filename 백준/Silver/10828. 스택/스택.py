import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

stack = deque()
for _ in range(N):
    cheak = list(input().split())
    if len(cheak) == 2:
        stack.append(int(cheak[1]))
    else:
        if cheak[0] == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                value = stack.pop()
                print(value)
        elif cheak[0] == "size":
            print(len(stack))
        elif cheak[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
            