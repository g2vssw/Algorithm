import sys

input = sys.stdin.readline

def combination(arr):
    
    result = []

    if len(arr) == M:
        result.append(arr)
        return result

    def backtrack(si, path):

        if len(path) == M:
            result.append(path[:])
            return
        
        for i in range(si, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])

    return result

N, M = map(int, input().split())

H_arr = []
C_arr = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            H_arr.append((i, j))
        elif row[j] == 2:
            C_arr.append((i, j))

C_result = combination(C_arr)

min_sum_c_dist = 21e8
for C_list in C_result:
    sum_c_dist = 0
    for h in H_arr:
        min_c_dist = 21e8
        for c in C_list:
            c_dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_c_dist = min(c_dist, min_c_dist)
        sum_c_dist += min_c_dist
    min_sum_c_dist = min(min_sum_c_dist, sum_c_dist)

print(min_sum_c_dist)