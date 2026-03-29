import sys

input = sys.stdin.readline

A, B = map(int, input().split())

C = int(input())

N = C // 60
M = C % 60

B += M

if B >= 60:
    B -= 60
    A += 1

A += N

A = A % 24

print(f"{A} {B}")