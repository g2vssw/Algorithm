import sys

input = sys.stdin.readline

def check(visited):
    start_team_score = 0
    link_team_score = 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start_team_score += arr[i][j]
            elif not visited[i] and not visited[j]:
                link_team_score += arr[i][j]

    return abs(start_team_score - link_team_score)

def dfs():

    min_result = 21e8
    visited = [False] * N

    def backtrack(si, cnt):
        nonlocal min_result
        
        if cnt == M:
            value = check(visited)
            min_result = min(min_result, value)
            return

        for i in range(si, N):
            if not visited[i]:
                visited[i] = True
                backtrack(i + 1, cnt + 1)
                visited[i] = False

                # 조기종료
                if min_result == 0:
                    return

    # # 0번 사람을 미리 스타트 팀에 넣고 시작 (대칭성 활용 + 절반 감소)
    visited[0] = True
    backtrack(1, 1)

    return min_result

N = int(input())

M = N // 2

arr = [list(map(int, input().split())) for _ in range(N)]

result = dfs()

print(result)