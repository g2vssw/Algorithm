def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        if len(phone_number) - 4 <= i <= len(phone_number) - 1:
            answer += phone_number[i]
        else:
            answer += "*"
    return answer