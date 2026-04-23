def Plus_123(n):
    if n == 0:
        return 1

    elif n < 0:
        return 0

    return Plus_123(n-1) + Plus_123(n-2) + Plus_123(n-3)

T = int(input())

for _ in range(T):
    N = int(input())
    print(Plus_123(N))