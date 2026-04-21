def com(L):
    global result
    global flag

    if L == N:
        num = int("".join(path))
        if num > X:
            if result < num:
                return
            else:
                flag = 1
                result = min(result, num)

    for i in range(N):
        if used[i]:
            continue
        else:
            used[i] = True
            path.append(li[i])
            com(L + 1)
            path.pop()
            used[i] = False

X = int(input())
li = list(str(X))
N = len(li)
path = []
used = [False] * N
result = 21e8
flag = 0

com(0)

if flag:
    print(result)
else:
    print(0)