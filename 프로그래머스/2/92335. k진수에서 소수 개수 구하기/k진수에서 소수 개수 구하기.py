def to_k_number(n, k):
    if n == 1:
        return "0"
    
    result = ""
    while n > 0:
        result += str(n % k)
        n = n // k
        
    return result[::-1]

def is_prime(n):
    
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def solution(n, k):
    answer = 0
    
    k_num = to_k_number(n, k)
    
    for s in k_num.split("0"):
        if s != "":
            if is_prime(int(s)):
                answer += 1

    return answer