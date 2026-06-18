def solution(picks, minerals):
    answer = 0
    
    total_picks = sum(picks)

    if total_picks == 0:
        return 0
    
    minerals = minerals[:total_picks * 5]
    
    minerals_arr = []
    
    for i in range(0, len(minerals), 5):
        mineral_uion = minerals[i:i+5]
        
        dia, iron, stone = 0, 0, 0
        for mineral in mineral_uion:
            if mineral == "diamond":
                dia += 1
            elif mineral == "iron":
                iron += 1
            else:
                stone += 1
        
        minerals_arr.append([dia, iron, stone])
    
    minerals_arr.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for d, i, s in minerals_arr:
        if picks[0]:
            picks[0] -= 1
            answer += (d + i + s)
        elif picks[1]:
            picks[1] -= 1
            answer += (d * 5 + i + s)
        else:
            picks[2] -= 1
            answer += (d * 25 + i * 5 + s)
                
    return answer