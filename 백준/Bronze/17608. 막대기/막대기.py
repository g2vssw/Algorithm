import sys

input = sys.stdin.readline

N = int(input())

stick_list = []
for _ in range(N):
    stick_list.append(int(input()))

cnt = 0
cheak = -1
for i in range(N - 1, -1, -1):
    if stick_list[i] > cheak:
        cheak = stick_list[i]
        cnt += 1

print(cnt)