def solution(survey, choices):
    answer = ''
    char = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            char[survey[i][0]] = char[survey[i][0]] - choices[i] + 4
        else:
            char[survey[i][1]] = char[survey[i][1]] + choices[i] - 4
    for c in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if char[c[0]] >= char[c[1]]:
            answer += c[0]
        else:
            answer += c[1]
    return answer