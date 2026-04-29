def solution(s):
    answer = []
    dp = [-1] * 26
    for i in range(len(s)):
        num = ord(s[i]) - 97
        if dp[num] == -1:
            answer.append(-1)
            dp[num] = i
        else:
            answer.append(i - dp[num])
            dp[num] = i
    return answer