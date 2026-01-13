def solution(numbers):
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    answer = ""
    s = 0
    for i in range(len(numbers) + 1):
        if numbers[s:i] in num_dict:
            answer += str(num_dict[numbers[s:i]])
            s = i
    return int(answer)