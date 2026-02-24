import sys

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]

arr.sort()

for r in arr:
    print(r)