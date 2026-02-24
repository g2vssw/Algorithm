import sys

input = sys.stdin.readline

def pick(arr):

    flag = 0

    def backtrack(path, si):
        nonlocal flag

        if X <= sum(path) <= Y:    
            flag = 1
            return
        
        if sum(path) > Y:
            return
        
        for i in range(si, len(arr)):
            path.append(arr[i])
            
            backtrack(path, i + 1)

            path.pop()

    backtrack([], 0)

    if flag:
        return "YES"
    else:
        return "NO"

T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    arr = list(map(int, input().split()))
    
    result = pick(arr)

    print(result)