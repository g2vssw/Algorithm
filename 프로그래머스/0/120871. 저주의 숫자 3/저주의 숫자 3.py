def solution(n):
    answer = 0
    cnt = 0
    s = 1
    e = n + 1
    while True:
        if s == e:
            answer = s - 1
            break
        for num in range(s, e):
            if num % 3 == 0 or "3" in str(num):
                cnt += 1
        s = e
        e = e + cnt
        cnt = 0
    return answer