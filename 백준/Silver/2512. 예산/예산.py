import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr_sum = sum(arr)

M = int(input())

start = 1
end = max(arr)
result = 0

if arr_sum <= M:
    result = max(arr)
else:
    while start <= end:
        middle = (start + end) // 2
        value = 0

        for num in arr:
            if middle >= num:
                value += num
            else:
                value += middle
        if value <= M:
            result = middle
            start = middle + 1
        else:
            end = middle - 1

print(result)