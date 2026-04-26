import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    line = input()
    stack = []

    for i in line:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')