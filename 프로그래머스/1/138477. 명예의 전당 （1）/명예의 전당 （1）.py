def solution(k, score):
    answer = []
    hf = []
    for s in score:
        hf.sort(reverse=True)
        if len(hf) < k:
            hf.append(s)
        else:
            if hf[-1] < s:
                hf.pop()
                hf.append(s)
        hf.sort(reverse=True)
        answer.append(hf[-1])
    return answer