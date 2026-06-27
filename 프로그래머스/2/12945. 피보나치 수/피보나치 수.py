import sys
sys.setrecursionlimit(100005)

def solution(n):
    dp = [-1] * 100001
    dp[0] = 0
    dp[1] = 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        def fido(num):
            nonlocal dp
            
            if dp[num] != -1:
                return dp[num]
            
            dp[num] = (fido(num - 1) + fido(num - 2)) % 1234567

            return dp[num]
        
        answer = fido(n)
    return answer