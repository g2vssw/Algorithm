def solution(n):
    answer = []
    cnt = 1
    while True:
        if cnt == n:
            answer.append(n)
            break
        if n % cnt == 0:
            answer.append(cnt)
        cnt += 1
    return answer