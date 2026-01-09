def solution(array):
    answer = 0
    dp = [0] * 1000
    for n in array:
        dp[n] += 1
    if dp.count(max(dp)) > 1:
        answer = -1
    else:
        answer = dp.index(max(dp))
    return answer