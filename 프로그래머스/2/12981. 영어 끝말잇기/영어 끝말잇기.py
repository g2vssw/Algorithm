def solution(n, words):
    used = set()
    used.add(words[0])

    for i in range(1, len(words)):
        # 끝말 규칙 또는 중복 단어 검사
        if words[i] in used or words[i-1][-1] != words[i][0]:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]

        used.add(words[i])

    return [0, 0]