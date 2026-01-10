def solution(num_list):
    hol = 0
    jja = 0
    for num in num_list:
        if num % 2 == 0:
            jja += 1
        else:
            hol += 1
    answer = [jja, hol]
    return answer