import sys
input = sys.stdin.readline

N, P = map(int, input().split())
line = [[] for _ in range(7)]

cnt = 0
for _ in range(N):
    l, n = map(int, input().split())

    if not line[l]:
        line[l].append(n)
        cnt += 1
    elif line[l]:
        if line[l][-1] < n:
            line[l].append(n)
            cnt += 1
        elif line[l][-1] >= n:
            while True:
                if not line[l] or line[l][-1] < n:
                    line[l].append(n)
                    cnt += 1
                    break
                elif line[l][-1] == n:
                    break
                else:
                    line[l].pop()
                    cnt += 1

print(cnt)