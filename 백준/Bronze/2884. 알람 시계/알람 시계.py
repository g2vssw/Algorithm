import sys

input = sys.stdin.readline

H, M = map(int, input().split())

if M >= 45:
    M -= 45
else:
    H -= 1
    if H < 0:
        H = 23
    M = M + 60 - 45

print(f'{H} {M}')