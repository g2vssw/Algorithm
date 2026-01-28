def solution(n):
    answer = ""
    li = list(str(n))
    li.sort()
    for n in li[::-1]:
        answer += n
    answer = int(answer)
    return answer