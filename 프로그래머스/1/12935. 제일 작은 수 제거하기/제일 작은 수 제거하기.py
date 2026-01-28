def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        sort_arr = sorted(arr)
        min_v = sort_arr[0]
        for n in arr:
            if n == min_v:
                continue
            else:
                answer.append(n)
    return answer