def solution(s):
    answer = ''
    s_list = list(map(int, s.split()))
    min_value = min(s_list)
    max_value = max(s_list)
    answer = str(min_value) + " " + str(max_value)
    return answer