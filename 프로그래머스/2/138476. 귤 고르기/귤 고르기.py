def solution(k, tangerine):
    answer = 0
    tangerine_dict = {}
    for size in tangerine:
        tangerine_dict[size] = tangerine_dict.get(size, 0) + 1
    tangerine_sort = sorted(tangerine_dict.items(), key=lambda x: -x[1])
    l = 0
    for key, value in tangerine_sort:
        answer += 1
        
        k -= value
        
        if k <= 0:
            break
    return answer