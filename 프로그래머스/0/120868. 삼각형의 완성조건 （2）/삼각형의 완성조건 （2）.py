def solution(sides):
    answer = 0
    set_v = set()
    max_v = max(sides)
    min_v = min(sides)
    for num1 in range(max_v, 0, -1):
        if max_v < num1 + min_v:
            set_v.add(num1)    
    answer += len(set_v)
    answer += sum(sides) - max_v - 1
    return answer