N = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

w_max = 0
w_max_idx = 0
l_max = 0
l_max_idx = 0

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w_max <= arr[i][1]:
            w_max = arr[i][1]
            w_max_idx = i
    else:
        if l_max <= arr[i][1]:
            l_max = arr[i][1]
            l_max_idx = i

s_w = abs(arr[(l_max_idx + 1) % 6][1] - arr[(l_max_idx - 1) % 6][1])
s_l = abs(arr[(w_max_idx + 1) % 6][1] - arr[(w_max_idx - 1) % 6][1])

result = (w_max * l_max - s_w * s_l) * N

print(result)