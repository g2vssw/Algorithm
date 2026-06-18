def solution(record):
    answer = []
    nickname_dict = {}
    
    temp = []
    for re in record:
        part = re.split()
        if len(part) == 3:
            action, user_id, user_nickname = part
        else:
            action, user_id = part
        if action == "Enter":
            nickname_dict[user_id] = user_nickname
            temp.append((action, user_id))
        elif action == "Leave":
            temp.append((action, user_id))
        else:
            nickname_dict[user_id] = user_nickname
    
    for action, user_id in temp:
        if action == "Enter":
            answer.append(f"{nickname_dict[user_id]}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname_dict[user_id]}님이 나갔습니다.")
    
    return answer