def solution(age):
    answer = ''
    for n in list(map(int, str(age))):
        answer += chr(n + 97)
    return answer