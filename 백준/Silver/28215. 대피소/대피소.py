import sys

input = sys.stdin.readline

# 대피소 경우의 수 조합
def combination(arr):
    # 모든 대피소 조합은 이중 리스트 안 튜플로 저장 [[(0, 1), (0, 2)], ... ]
    result = []

    def backtrack(si, path):
        
        # path의 길이가 대피소의 수 K와 같아지면 return
        if len(path) == K:
            # path[:] 사용해 append
            result.append(path[:])
            return

        # 조합으로 visited는 활용하지 안고 시작 인덱스 si를 활용해 range 범위를 조정
        for i in range(si, N):
            # 백트래킹
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    # 조합: 시작 인덱스 si를 활용해 range 범위를 조정, 빈 리스트 path
    backtrack(0, [])

    return result

# N개의 집, K개의 집에 대피소를 설치
N, K = map(int, input().split())

# 정수 범위를 고려하여 무한 값 지정
INF = float("INF")

# 모든 집의 위치 arr
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

# 조합
result = combination(arr)

# 최종 결과 값: 대피소를 설치하는 모든 방법 중 가장 가까운 대피소와 집 사이의 거리 중 가장 큰 값이 가장 작을 때의 거리
min_value = INF
for shelters in result:
    # 각 집의 최소 거리들 중 가장 큰 값(N = K일 경우를 고려 하여 기본 값을 0으로 설정)
    max_dist = 0
    for home in arr:
        # 보호소로 지정된 집에 경우 continue
        if home in shelters:
            continue
        # 집을 기준으로 가장 가까운 거리
        min_dist = INF
        for shelter in shelters:
            # 맨해튼 거리 계산
            dist = abs(home[0] - shelter[0]) + abs(home[1] - shelter[1])
            # 집을 기준으로 대피소 중 가장 가까운 거리를 선택
            min_dist = min(min_dist, dist)
        # 각 집의 최소 거리들 중 가장 큰 값을 찾음
        max_dist = max(max_dist, min_dist)
    # 최대 거리들 중 전체 최솟값을 갱신
    min_value = min(min_value, max_dist)

print(min_value)