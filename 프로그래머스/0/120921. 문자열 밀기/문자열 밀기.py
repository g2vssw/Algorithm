def solution(A, B):
    answer = 21e8
    n = len(A)
    for i in range(n):
        C = A[-i:] + A[:-i]
        if B == C:
            answer = min(answer, i)
    if answer == 21e8:
        answer = -1
    return answer