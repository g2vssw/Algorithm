def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    shot = -1
    for s, e in targets:
        if s >= shot:
            answer += 1
            shot = e
    return answer