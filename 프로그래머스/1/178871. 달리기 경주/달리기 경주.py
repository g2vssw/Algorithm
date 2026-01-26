def solution(players, callings):
    players_dict = {}
    for i in range(len(players)):
        players_dict[players[i]] = i

    for name in callings:
        i = players_dict[name]
        players[i], players[i - 1] = players[i - 1], players[i]
        players_dict[name] -= 1
        players_dict[players[i]] += 1
    
    answer = players
    
    return answer