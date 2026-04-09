li = [0] * 31

for _ in range(28):
    N = int(input())
    li[N] = 1

for i in range(1, 31):
    if li[i] == 0:
        print(i)