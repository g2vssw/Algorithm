import sys

input = sys.stdin.readline

def dfs():
    result_set = set()
    visited = [False] * N

    def backtrack(path):
        
        if len(path) == K:
            r = "".join(path)
            result_set.add(r)
            return
        
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                path.append(str(cards[i]))

                backtrack(path)

                path.pop()
                visited[i] = False

        return

    backtrack([])

    return len(result_set)

N = int(input())
K = int(input())

cards = [int(input()) for _ in range(N)]

result = dfs()

print(result)