def solution(arr, delete_list):
    answer = []
    for s1 in arr:
        flag = 0
        for s2 in delete_list:
            if s1 == s2:
                flag = 1
                break
        if flag == 0:
            answer.append(s1)
            
    return answer