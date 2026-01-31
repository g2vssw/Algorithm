def solution(a, b):
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    dict_2016 = {1: 0, 2: 31, 3: 60, 4: 91,
                 5: 121, 6: 152, 7: 182, 8: 213,
                 9: 244, 10: 274, 11: 305, 12: 335
                }
    value = dict_2016[a] + b - 1
    idx = value % 7
    answer = week[idx]
    return answer