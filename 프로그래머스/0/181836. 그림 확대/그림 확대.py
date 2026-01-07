def solution(picture, k):
    answer = []
    for ss in picture:
        strx = ""
        for s in ss:
            for _ in range(k):
                strx += s
        for _ in range(k):
            answer.append(strx)
    return answer