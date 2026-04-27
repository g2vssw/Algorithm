import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    p = input().strip() # 수행할 함수 (예: RDD)
    n = int(input())    # 배열에 들어있는 수의 개수
    
    # [1,2,3,4] 형태의 문자열을 리스트로 변환
    # 숫자가 없는 경우([])를 위해 n을 체크하여 처리
    raw_arr = input().strip()[1:-1]
    if n == 0:
        dq = deque()
    else:
        dq = deque(raw_arr.split(','))

    # 2. 변수 초기화
    is_reversed = False # 현재 뒤집힌 상태인지 확인하는 플래그
    is_error = False    # 에러 발생 여부

    # 3. 명령어 수행
    for cmd in p:
        if cmd == 'R':
            # 실제로 뒤집지 않고 상태만 반전
            is_reversed = not is_reversed
        elif cmd == 'D':
            if not dq:
                is_error = True
                break
            # 뒤집힌 상태에 따라 앞 또는 뒤에서 제거
            if is_reversed:
                dq.pop()
            else:
                dq.popleft()

    # 4. 결과 출력
    if is_error:
        print("error")
    else:
        # 마지막 상태가 뒤집힌 상태라면 리스트를 실제로 한 번 뒤집어줌
        if is_reversed:
            dq.reverse()
        # 결과 형식 [1,2,3]에 맞춰 출력
        print("[" + ",".join(dq) + "]")

# 테스트 케이스 개수만큼 반복
T = int(input())
for _ in range(T):
    solve()