from collections import deque

N = int(input())

li = deque()
for _ in range(N):
    n = int(input())
    li.append(n)

D = deque()
for num in range(1, N+1):
    D.append(num)

pm = []
R = deque()
while D:
    R.append(D.popleft())
    pm.append("+")
    while R:
        if li[0] != R[-1]:
            break
        elif li[0] == R[-1]:
            R.pop()
            li.popleft()
            pm.append("-")

if li:
    print("NO")
else:
    for result in pm:
        print(result)