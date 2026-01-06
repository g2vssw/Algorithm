def chk(s, e):
    global cnt, c_s, c_e

    if c_e <= s:
        c_s = s
        c_e = e
        cnt += 1
    else:
        return

N = int(input())

li = []
for _ in range(N):
    s, e = map(int, input().split())
    li.append((e, s))

li.sort()

cnt = 0
c_s, c_e = -1, -1
for e, s in li:
    chk(s, e)

print(cnt)