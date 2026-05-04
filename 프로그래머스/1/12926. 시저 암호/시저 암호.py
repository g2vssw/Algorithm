def solution(s, n):
    answer = ''
    for t in s:
        if t == " ":
            answer += t
        elif t.islower():
            answer += chr((ord(t) - ord('a') + n) % 26 + ord('a'))
        elif t.isupper():
            answer += chr((ord(t) - ord('A') + n) % 26 + ord('A'))
    return answer