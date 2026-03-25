import sys

input = sys.stdin.readline

f_num = int(input().strip())
s_num = str(input().strip())

for num in s_num[::-1]:
    print(f_num * int(num))

print(f_num * int(s_num))