def check(want, want_dict, discount_dict):
    for good in want:
        if want_dict[good] > discount_dict.get(good, 0):
            return False
    return True

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    discount_dict = {}
    for i in range(10):
        discount_dict[discount[i]] = discount_dict.get(discount[i], 0) + 1
    
    if check(want, want_dict, discount_dict):
        answer += 1
    
    for i in range(1, len(discount) - 9):
        discount_dict[discount[i - 1]] -= 1
        discount_dict[discount[i + 9]] = discount_dict.get(discount[i + 9], 0) + 1
        if check(want, want_dict, discount_dict):
            answer += 1
    return answer