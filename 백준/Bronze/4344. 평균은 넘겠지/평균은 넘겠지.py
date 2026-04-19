N = int(input())

for _ in range(N):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for score in scores[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt / scores[0] * 100
    print(f'{rate:.3f}%')