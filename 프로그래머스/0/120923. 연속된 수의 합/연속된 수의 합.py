def solution(num, total):
    answer = []
    a = total / num - ((num + 1) / 2)
    for i in range(1, num + 1):
        answer.append(a + i)
    return answer