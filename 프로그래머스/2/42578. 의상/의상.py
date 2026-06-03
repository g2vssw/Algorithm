def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        clothes_dict[cloth[1]] = clothes_dict.get(cloth[1], 0) + 1
    
    value = 1
    for cloth in clothes_dict:
        value *= (clothes_dict[cloth] + 1)
    
    answer = value - 1
    
    return answer