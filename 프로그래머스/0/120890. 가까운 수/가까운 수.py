def solution(array, n):
    answer = 0
    min_sub = 21e8
    for num in array:
        if abs(n - num) == min_sub:
            if answer > num:
                answer = num
        elif abs(n - num) < min_sub:
            min_sub = abs(n - num)
            answer = num
    return answer