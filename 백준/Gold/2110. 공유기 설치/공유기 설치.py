import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(int(input()) for _ in range(N))
arr.sort()

# start와 end 사이의 숫자 중 정답(최적의 거리)을 찾을 것
start = 1  # 두 공유기 사이의 가능한 최소 거리
end = arr[-1] - arr[0]  # 두 공유기 사이의 가능한 최대 거리
result = 0

while start <= end:
    # 목표로 하는 두 공유기 사이의 최소 거리: middle
    middle = (start + end) // 2
    current = arr[0]  # 공유기 사이의 간격을 최대한 넓게 만드는 것이 목표임으로 첫 번째 집부터 설치
    router = 1  # 첫 집에 설치

    # 두 번째 집부터 순회하며 확인: 집들 사이의 거리를 무조건 middle 이상 띄워서 설치
    for i in range(1, len(arr)):
        # 가장 마지막으로 공유기를 설치한 집으로부터 확인하는 집이 middle 이상 떨어져 있는지 확인
        if arr[i] >= current + middle:
            # 떨어져 있다면 공유기를 설치하고 router(공유기) += 1
            current = arr[i]
            router += 1
    
    # 거리를 middle로 잡았는데 공유기 M개를 모두 설치할 수 있다면?
    if router >= M:
        # 정답 후보 저장 후 더 넓은 간격으로도 설치할 수 있는지 확인: 탐색 범위를 오른쪽으로 좁힘(middle을 늘림)
        result = middle
        start = middle + 1
    # 거리를 middle로 잡았는데 공유기 M개를 모두 설치할 수 없다면?
    else:
        # 더 좁은 간격으로도 설치할 수 있는지 확인: 탐색 범위를 왼쪽으로 좁힘(middle을 줄임)
        end = middle - 1

print(result)