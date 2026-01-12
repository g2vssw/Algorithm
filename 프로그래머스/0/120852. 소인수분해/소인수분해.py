def solution(n):
    answer = set()
    m = n
    so = 2
    while True:
        if m == 1:
            break
        if m % so == 0:
            m = m // so
            answer.add(so)
            continue
        so += 1
    return sorted(list(answer))