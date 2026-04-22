import sys
input = sys.stdin.readline

S = list(input().strip())
B = list(input().strip())
N = len(S)
X = len(B)

stack = []

for i in range(N):
    stack.append(S[i])

    if stack[-1] == B[-1]:
        if stack[-X:] == B[-X:]:
            for _ in range(X):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")