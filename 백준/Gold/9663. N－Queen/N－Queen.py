import sys

input = sys.stdin.readline

def n_queen():

    if N == 1:
        return 1
    
    cnt = 0

    # 체크용 배열: 세로, / 대각선, \ 대각선을 사용하였는지
    used_cols = [False] * N # 열 방향
    # N이 8일 경우 (0, 0)인 0부터 (N - 1) + N = 2N - 1인 15까지: used_diag2일 경우 N을 더해 양수로 사용 처리 하기 때문에
    used_diag1 = [False] * (2 * N) # / 방향 (r+c): 인덱스 최솟값 0 ~ 최댓값 2N - 2
    used_diag2 = [False] * (2 * N) # \ 방향 (r-c): N을 더해 양수로 사용 처리 인덱스 최솟값 1 ~ 최댓값 2N - 1

    def backtrack(row):
        nonlocal cnt

        if row == N:
            cnt += 1
            return
        
        # row마다 하나의 Queen
        for col in range(N):
            # 모두 False면 사용처리: \ 대각선의 경우 (r-c)시 음수가 존재할 수 있음으로 N을 더해 양수로 사용 처리([row - col + N])
            if not (used_cols[col] or used_diag1[row + col] or used_diag2[row - col + N]):
                used_cols[col] = used_diag1[row + col] = used_diag2[row - col + N] = True
                backtrack(row + 1)
                used_cols[col] = used_diag1[row + col] = used_diag2[row - col + N] = False

    backtrack(0)

    return cnt

N = int(input())

result = n_queen()

print(result)