def solution(numbers, hand):
    answer = ''
    keypad_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                   4: (1, 0), 5: (1, 1), 6: (1, 2),
                   7: (2, 0), 8: (2, 1), 9: (2, 2),
                   "*": (3, 0), 0: (3, 1), "#": (3, 2)}
    L = "*"
    R = "#"
    for number in numbers:
        if number in [1, 4, 7]:
            L = number
            answer += "L"
        elif number in [3, 6, 9]:
            R = number
            answer += "R"
        else:
            L_v = abs(keypad_dict[L][0] - keypad_dict[number][0]) + abs(keypad_dict[L][1] - keypad_dict[number][1])
            R_v = abs(keypad_dict[R][0] - keypad_dict[number][0]) + abs(keypad_dict[R][1] - keypad_dict[number][1])
            if L_v < R_v:
                L = number
                answer += "L"
            elif L_v > R_v:
                R = number
                answer += "R"
            else:
                if hand == "left":
                    L = number
                    answer += "L"
                else:
                    R = number
                    answer += "R"
    return answer