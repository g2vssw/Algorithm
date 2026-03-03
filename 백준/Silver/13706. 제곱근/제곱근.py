import sys

input = sys.stdin.readline

N = int(input())

start = 0
end = N
result = 0

while start <= end:
    middle = (start + end) // 2
    square = middle * middle

    if square == N:
        result = middle
        break
    elif square < N:
        start = middle + 1
    else:
        end = middle - 1

print(result)