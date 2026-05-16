def solution(participant, completion):
    answer = ''
    completion_dict = {}
    for name in participant:
        completion_dict[name] = completion_dict.get(name, 0) + 1
    for name in completion:
        completion_dict[name] -= 1
    for name in completion_dict:
        if completion_dict[name] > 0:
            answer = name
    return answer