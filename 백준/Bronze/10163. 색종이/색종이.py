N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]

arr = [[0 for _ in range(1001)] for _ in range(1001)]

for num in range(N):
    for i in range(num_list[num][0], num_list[num][0] + num_list[num][2]):
        for j in range(num_list[num][1], num_list[num][1] + num_list[num][3]):
            arr[i][j] = num + 1

for i in range(1, N + 1):
    num = 0
    for li in arr:
        num += li.count(i)
    print(num)
    num = 0