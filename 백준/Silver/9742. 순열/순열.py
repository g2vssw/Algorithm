import sys

input = sys.stdin.readline

def permutation(arr):
    visited =[False] * len(arr)
    cnt = [0]

    def backtrack(path):
        
        if len(path) == len(arr):
            cnt[0] += 1
            if cnt[0] == N:
                return path
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                path.append(arr[i])

                result = backtrack(path)

                if result:
                    return result
                
                path.pop()
                visited[i] = False
        
        return

    return backtrack([])
    
    
while True:
    inputs = input().split()
    
    if len(inputs) != 2:
        break

    S, N = inputs
    S_list = list(S)
    N = int(N)

    result = permutation(S_list)

    if result:
        print(f'{S} {N} = {"".join(result)}')
    else:
        print(f'{S} {N} = No permutation')