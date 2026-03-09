import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

result = 0
if A == B == C:
    result = 10000 + A * 1000
elif (A == B and B != C) or (B == C and C != A) or (C == A and A != B):
    if B == C:
        result = 1000 + B * 100
    else:
        result = 1000 + A * 100
elif A != B and B != C and C != A:
    result = max(A, B, C) * 100

print(result)