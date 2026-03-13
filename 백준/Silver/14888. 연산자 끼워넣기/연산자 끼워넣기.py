import sys

input = sys.stdin.readline

def dfs():

    max_result = -21e8
    min_result = 21e8

    def backtrack(n, value):
        nonlocal max_result
        nonlocal min_result

        if n == N - 1:
           max_result = max(max_result, value)
           min_result = min(min_result, value)
           return

        if operators[0] != 0:
            operators[0] -= 1
            backtrack(n + 1, value + arr[n+1])
            operators[0] += 1
        if operators[1] != 0:
            operators[1] -= 1
            backtrack(n + 1, value - arr[n+1])
            operators[1] += 1
        if operators[2] != 0:
            operators[2] -= 1
            backtrack(n + 1, value * arr[n+1])
            operators[2] += 1
        if operators[3] != 0:
            operators[3] -= 1
            backtrack(n + 1, int(value / arr[n+1]))
            operators[3] += 1

    backtrack(0, arr[0])

    return max_result, min_result

N = int(input())

arr = list(map(int, input().split()))

# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
operators = list(map(int, input().split()))

max_result, min_result = dfs()

print(max_result)
print(min_result)