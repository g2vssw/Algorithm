import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    middle = (start + end) // 2
    value = 0
    for tree in arr:
        if tree > middle:
            value += (tree - middle)
    if value >= M:
        result = middle
        start = middle + 1
    else:
        end = middle - 1

print(result)