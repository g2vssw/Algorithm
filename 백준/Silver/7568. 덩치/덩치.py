N = int(input())

member = []
for _ in range(N):
    x, y = map(int, input().split())
    member.append([x, y])
cnt = [1] * N

for i in range(N):
    c = member[i]
    for j in range(N):
        if c[0] < member[j][0] and c[1] < member[j][1]:
            cnt[i] += 1

print(*cnt)