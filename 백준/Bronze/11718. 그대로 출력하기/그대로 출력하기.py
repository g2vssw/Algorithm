import sys

# sys.stdin.readline으로 입력 받기
input = sys.stdin.readline

# 입력을 계속해서 받기
while True:
    line = input().strip()
    if not line:  # 빈 줄이 입력되면 종료
        break
    print(line)