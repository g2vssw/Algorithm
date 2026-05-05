def solution(answers):
    answer = []
    li = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    m_v = -1
    for i in range(3):
        v = 0
        for j in range(len(answers)):
            n = j % len(li[i])
            if answers[j] == li[i][n]:
                v += 1
        if v > m_v:
            answer = []
            answer.append(i + 1)
            m_v = v
        elif v == m_v:
            answer.append(i + 1)
        
    return answer