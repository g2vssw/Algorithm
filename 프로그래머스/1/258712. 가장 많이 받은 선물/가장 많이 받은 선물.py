def solution(friends, gifts):
    answer = 0
    friends_dict = {}
    answer_dict = {}
    
    for friend in friends:
        friends_dict[friend] = [[0, 0]]
        answer_dict[friend] = 0
    
    for gift in gifts:
        f, t = gift.split()
        friends_dict[f][0][0] += 1
        friends_dict[t][0][1] += 1
        friends_dict[f].append(t)
        
    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            f = friends[i]
            b = friends[j]
            if friends_dict[f].count(b) > friends_dict[b].count(f):
                answer_dict[f] += 1
            elif friends_dict[f].count(b) < friends_dict[b].count(f):
                answer_dict[b] += 1
            else:
                if (friends_dict[f][0][0] - friends_dict[f][0][1]) > (friends_dict[b][0][0] - friends_dict[b][0][1]):
                    answer_dict[f] += 1
                elif (friends_dict[f][0][0] - friends_dict[f][0][1]) < (friends_dict[b][0][0] - friends_dict[b][0][1]):
                    answer_dict[b] += 1
                else:
                    continue
    
    for friend in friends:
        answer = max(answer, answer_dict[friend])
    
    return answer