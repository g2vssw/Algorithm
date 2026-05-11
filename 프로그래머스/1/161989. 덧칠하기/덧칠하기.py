def solution(n, m, section):
    answer = 0
    wall = [0] * (n + 1)
    for i in range(len(section)):
        idx = section[i]
        if wall[idx] == 0:
            answer += 1
            for j in range(m):
                if idx+j > n:
                    continue
                wall[idx+j] = 1
    return answer