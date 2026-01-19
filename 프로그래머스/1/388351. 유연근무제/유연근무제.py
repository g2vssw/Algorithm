def time_10(time):
    if time % 100 + 10 >= 60:
        time = ((time // 100 + 1) * 100) + ((time % 100) - 50)
        return time
    else:
        return time + 10

def solution(schedules, timelogs, startday):
    answer = 0
    flag = 0
    for i in range(len(schedules)):
        for j in range(startday, startday + 7):
            day = j // 8 + j % 8
            end_time = time_10(schedules[i])
            if day == 6 or day == 7:
                continue
            if timelogs[i][j - startday] <= end_time:
                continue
            else:
                flag = 1
                break
        if flag == 0:
            answer += 1
        else:
            flag = 0
    return answer