import sys

input = sys.stdin.readline

# 신호등의 개수 N, 도로의 길이 L
N, L = map(int, input().split())

# 신호등의 위치 D, 빨간색 지속 시간 R, 초록색 지속 시간 G
traffic_light_dict = {}
for _ in range(N):
    D, R, G = map(int, input().split())
    traffic_light_dict[D] = (R, G)

# 출발 후 시간 흐름
result = 0
for i in range(1, L + 1):
    result += 1
    if i in traffic_light_dict:
        v = result % (traffic_light_dict[i][0] + traffic_light_dict[i][1])
        if v < traffic_light_dict[i][0]:
            result += (traffic_light_dict[i][0] - v)
    
print(result)