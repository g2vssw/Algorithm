import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = []
stack = []
for i in range(len(arr)):
    num = arr[i]
    if len(stack) == 0:
        stack.append((i, num))
        result.append(-1)
    else:
        while stack:
            si, s = stack.pop()
            if s >= num:
                stack.append((si, s))
                break
            result[si] = num
        stack.append((i, num))
        result.append(-1)

print(" ".join(map(str, result)))