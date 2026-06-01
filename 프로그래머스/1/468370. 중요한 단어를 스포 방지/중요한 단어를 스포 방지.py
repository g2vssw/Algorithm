def solution(message, spoiler_ranges):
    spoiler_dp = [False] * len(message)
    for s_i, e_i in spoiler_ranges:
        for i in range(s_i, e_i + 1):
            spoiler_dp[i] = True
    
    spoiler_words = set()
    normal_words = set()
    temp = ""
    cheak = False
    for i in range(len(message)):
        if message[i] == " ":
            if temp != "":
                if cheak:
                    spoiler_words.add(temp)
                else:
                    normal_words.add(temp)
            temp = ""
            cheak = False
        else:
            if cheak:
                temp += message[i]
            else:
                if spoiler_dp[i]:
                    cheak = True
                    temp += message[i]
                else:
                    temp += message[i]
    
    if temp != "":
        if cheak:
            spoiler_words.add(temp)
        else:
            normal_words.add(temp)
                    
    answer = len(spoiler_words - normal_words)
        
    return answer