def solution(s):
    num_eng_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    num = ""
    str_num = ""
    for str_s in s:
        if str_s in "0123456789":
            num += str_s
        else:
            str_num += str_s
            if num_eng_dict.get(str_num):
                num += num_eng_dict.get(str_num)
                str_num = ""
            else:
                continue
    answer = int(num)
    return answer