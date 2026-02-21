import sys

input = sys.stdin.readline

def permutation(arr):
    result = []
    visited = [False] * N

    def backtrack(path):
        
        if len(path) == N:
            result.append(path[:])
            return
        
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                path.append(str(arr[i]))

                backtrack(path)

                path.pop()
                visited[i] = False

    backtrack([])

    return result

N = int(input())

arr = [i for i in range(1, N + 1)]

result = permutation(arr)

for r in result:
    print(" ".join(r))