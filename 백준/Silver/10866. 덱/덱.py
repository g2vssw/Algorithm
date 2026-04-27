import sys
from collections import deque # 덱 자료구조를 사용하기 위해 임포트

input = sys.stdin.readline

# 1. 명령의 수 N 입력
N = int(input())

# 2. 덱(Deque) 생성
# 파이썬의 deque는 내부적으로 양방향 연결 리스트로 구현되어 있어
# 앞, 뒤에서의 삽입과 삭제가 모두 O(1)임을 보장함
dq = deque()

# 3. N개의 명령 처리
for _ in range(N):
    # 명령어를 공백 기준으로 나누어 리스트로 저장
    command = input().split()
    
    # 각 명령어에 따른 분기 처리
    cmd_type = command[0]

    if cmd_type == "push_front":
        # 덱의 앞에 삽입
        dq.appendleft(command[1])

    elif cmd_type == "push_back":
        # 덱의 뒤에 삽입
        dq.append(command[1])

    elif cmd_type == "pop_front":
        # 덱의 가장 앞에 있는 수를 빼고 출력. 없으면 -1
        if dq:
            print(dq.popleft())
        else:
            print("-1")

    elif cmd_type == "pop_back":
        # 덱의 가장 뒤에 있는 수를 빼고 출력. 없으면 -1
        if dq:
            print(dq.pop())
        else:
            print("-1")

    elif cmd_type == "size":
        # 덱에 들어있는 정수의 개수 출력
        print(len(dq))

    elif cmd_type == "empty":
        # 덱이 비어있으면 1, 아니면 0 출력
        print(1 if not dq else 0)

    elif cmd_type == "front":
        # 덱의 가장 앞에 있는 정수 출력. 없으면 -1
        if dq:
            print(dq[0])
        else:
            print("-1")

    elif cmd_type == "back":
        # 덱의 가장 뒤에 있는 정수 출력. 없으면 -1
        if dq:
            print(dq[-1])
        else:
            print("-1")