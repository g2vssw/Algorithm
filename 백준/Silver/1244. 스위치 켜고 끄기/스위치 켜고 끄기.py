def switch(s):
    global li
    if li[s] == 1:
        li[s] = 0
    else:
        li[s] = 1

N = int(input())
li = list(map(int, input().split()))
S_N = int(input())

for _ in range(S_N):
    G, T = map(int, input().split())

    if G == 1:
        for i in range(T-1, N, T):
            switch(i)
    else:
        switch(T-1)
        for i in range(1, N):
            if T-1-i < 0 or T-1+i >= N:
                continue
            elif li[T - 1 - i] == li[T - 1 + i]:
                switch(T - 1 - i)
                switch(T - 1 + i)
            else:
                break

for i in range(N):
    print(li[i], end=' ')
    if i % 20 == 19:
        print()