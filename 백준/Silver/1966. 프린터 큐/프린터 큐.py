from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    D = deque()
    idx = deque()

    for i in range(N):
        D.append(li[i])
        idx.append(i)

    cnt = 0
    while True:
        if N == 1:
            cnt += 1
            print(cnt)
            break
        elif D[0] < max(D):
            D.append(D.popleft())
            idx.append(idx.popleft())
        elif D[0] == max(D):
            if idx[0] != M:
                D.popleft()
                idx.popleft()
                cnt += 1
            elif idx[0] == M:
                cnt += 1
                print(cnt)
                break