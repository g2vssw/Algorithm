N = int(input())

cnt = 0
for num in range(1, N+1):
    if 1 <= num <= 9:
        cnt += 1
    elif 10 <= num <= 99:
        cnt += 1
    elif 100 <= num <= 999:
        h = num // 100
        t = (num % 100) // 10
        o = num % 10
        if h - t == t - o:
            cnt += 1

print(cnt)