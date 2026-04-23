from collections import deque

li = deque(input())

D = deque()
R = deque()

flag = 0
while li:
    if li[0] == "<":
        flag = 1
        R.append(li.popleft())
        while True:
            if li[0] != ">":
                R.append(li.popleft())
            elif li[0] == ">":
                R.append(li.popleft())
                flag = 0
                break
    elif li[0] != "<" and flag == 0:
        D.append(li.popleft())
        while li:
            if li[0] != " " and li[0] != "<":
                D.append(li.popleft())
            elif li[0] == " " or li[0] == "<":
                if D:
                    while D:
                        R.append(D.pop())
                else:
                    if li[0] == "<":
                        break
                    R.append(li.popleft())
                    break

        while D:
            R.append(D.pop())

for r in R:
    print(r, end='')