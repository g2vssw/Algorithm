from collections import deque

N = int(input())

cnt = 0
for _ in range(N):
    S = list(input())
    stack = deque()

    for s in S:
        if len(stack) == 0:
            stack.append(s)
        elif stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    if len(stack) == 0:
       cnt += 1

print(cnt)