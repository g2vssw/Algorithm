import sys

input = sys.stdin.readline

N = int(input())
size_list = list(map(int, input().split()))
T, P = map(int, input().split())

T_cnt = 0
for size in size_list:
    if size == 0:
        continue
    T_cnt += (size + T - 1) // T
    
print(T_cnt)
print(f'{N // P} {N % P}')