import sys

input = sys.stdin.readline

def question(arr):

    cnt = 0

    def backtrack(si, path):
        nonlocal cnt
        
        if len(path) >= 2:
            if L <= sum(path) <= R and path[-1] - path[0] >= X:
                 cnt += 1

        if sum(path) > R:
                    return

        for i in range(si, N):
                path.append(arr[i])
                backtrack(i + 1, path)
                path.pop()

    backtrack(0, [])

    return cnt

N, L, R, X = map(int, input().split())

Q_list = list(map(int, input().split()))
Q_list.sort()

result = question(Q_list)

print(result)