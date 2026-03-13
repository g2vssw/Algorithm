import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N, M = map(int, input().split())

    result = 1
    if N == M:
        print(result)
    else:
        n = N
        m = M
        value1 = 1
        value2 = 1
        while True:
            if n == 0:
                break
            value1 *= m
            value2 *= n
            m -= 1
            n -= 1

        result = int(value1 // value2)

        print(result)