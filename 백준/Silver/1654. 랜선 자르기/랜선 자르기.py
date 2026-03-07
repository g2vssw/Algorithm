import sys

input = sys.stdin.readline

K, N = map(int, input().split())

arr = list(int(input()) for _ in range(K))

start = 1
end = max(arr)
result = 0

while start <= end:
    middle = (start + end) // 2
    value = 0

    for lan in arr:
        quotient = lan // middle
        if quotient:
            value += quotient

    if value >= N:
        result = middle
        start = middle + 1
    else:
        end = middle - 1

print(result)