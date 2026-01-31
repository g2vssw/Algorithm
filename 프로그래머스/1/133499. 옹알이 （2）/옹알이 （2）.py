def solution(babbling):
    answer = 0
    for word in babbling:
        si = 0
        ei = 1
        cheak = ""
        while ei < len(word) + 1:
            if word[si:ei] in ["aya", "ye", "woo", "ma"]:
                if cheak == word[si:ei]:
                    break
                else:
                    cheak = word[si:ei]
                    si = ei
                    ei += 1
            else:
                ei += 1
        if si == len(word):
            answer += 1
    return answer