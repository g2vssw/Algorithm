N = int(input())
switch = list(map(int, input().split()))
stu_num = int(input())

for _ in range(stu_num):
    G, T = map(int, input().split())

    if G == 1:
        for i in range(T-1, N, T):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    else:
        if switch[T-1] == 0:
            switch[T-1] = 1
        else:
            switch[T-1] = 0

        for i in range(1, N // 2):
            if T - 1 - i < 0 or T - 1 + i >= N:
                continue
            elif switch[T - 1 - i] == switch[T - 1 + i]:
                if switch[T - 1 - i] == 0:
                    switch[T - 1 - i] = 1
                    switch[T - 1 + i] = 1
                else:
                    switch[T - 1 - i] = 0
                    switch[T - 1 + i] = 0
            else:
                break

for i in range(N):
    print(switch[i], end=" ")
    if i % 20 == 19:
        print()