def solution(score):
    answer = score
    li = []
    for i in range(len(score)):
        li.append((sum(score[i]), score[i]))
    li.sort()
    cheak = 0
    rank = 1
    plus = 0
    for ss, s in li[::-1]:
        if ss == cheak:
            i = answer.index(s)
            answer[i] = rank
            plus += 1
        else:
            cheak = ss
            rank += plus
            plus = 0
            i = answer.index(s)
            answer[i] = rank
            plus += 1
    return answer