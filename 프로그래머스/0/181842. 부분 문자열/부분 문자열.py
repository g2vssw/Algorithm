def solution(str1, str2):
    answer = 1
    cheak = str2.find(str1)
    if cheak == -1:
        answer = 0
    return answer