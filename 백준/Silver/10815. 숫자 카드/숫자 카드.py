N = int(input())
san_li = set(map(int, input().split()))
M = int(input())
check_li = list(map(int, input().split()))


for i in range(M):
    if check_li[i] in san_li:
        check_li[i] = 1
    else:
        check_li[i] = 0

print(*check_li)