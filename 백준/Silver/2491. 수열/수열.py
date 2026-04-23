N = int(input())
li = list(map(int, input().split()))

cnt_max = 1
cnt = 1
for i in range(1, N):
    if li[i-1] <= li[i]:
        cnt += 1
    elif li[i - 1] > li[i]:
        cnt_max = max(cnt_max, cnt)
        cnt = 1

cnt_max = max(cnt_max, cnt)

cnt = 1
for i in range(1, N):
    if li[i-1] >= li[i]:
        cnt += 1
    elif li[i - 1] < li[i]:
        cnt_max = max(cnt_max, cnt)
        cnt = 1

cnt_max = max(cnt_max, cnt)

print(cnt_max)