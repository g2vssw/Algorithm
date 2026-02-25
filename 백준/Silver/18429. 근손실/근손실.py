import sys

input = sys.stdin.readline

def permutation(arr):
    
    # 경우의 수 count
    cnt = 0
    # 순열: visited 활용
    visited = [False] * N

    def backtrack(w, d):
        # nonlocal를 사용하여 cnt + 1
        nonlocal cnt
        
        # 만약 w가 500 미만이면 return
        if w < 500:
            return

        # 날짜 d가 N와 같아지면 cnt + 1 하고 return
        if d == N:
            cnt += 1
            return

        for i in range(N):
            # 백트래킹: 순열을 위한 visited, 중량 증가, 근손실
            if not visited[i]:
                visited[i] = True
                w += arr[i]
                w -= K
                backtrack(w, d + 1)
                w += K
                w -= arr[i]
                visited[i] = False

    # 순열: 운동 중량 w, 날짜 d
    backtrack(500, 0)

    return cnt

# N(총 일 수, 운동 키트 수), K(중량 감소량)
N, K = map(int, input().split())

# 각 운동 키트의 중량 증가량
arr = list(map(int, input().split()))

result = permutation(arr)

print(result)