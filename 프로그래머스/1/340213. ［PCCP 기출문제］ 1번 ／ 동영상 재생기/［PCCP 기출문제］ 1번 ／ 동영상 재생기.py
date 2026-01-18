def time_t(t_s):
    t_li = list(map(int, t_s.split(":")))
    t = t_li[0] * 60 + t_li[1]
    return t

def solution(video_len, pos, op_start, op_end, commands):
    video_len_t = time_t(video_len)
    pos_t = time_t(pos)
    if time_t(op_start) <= pos_t < time_t(op_end):
        pos_t = time_t(op_end)
    for c in commands:
        if c == "next":
            pos_t += 10
        elif c == "prev":
            pos_t -= 10
        if time_t(op_start) <= pos_t < time_t(op_end):
            pos_t = time_t(op_end)
        if pos_t < 0:
            pos_t = 0
        elif pos_t > video_len_t:
            pos_t = video_len_t
        if time_t(op_start) <= pos_t < time_t(op_end):
            pos_t = time_t(op_end)
    if len(str(pos_t // 60)) == 1:
        s = "0" + str(pos_t // 60)
    else:
        s = str(pos_t // 60)
    if len(str(pos_t % 60)) == 1:
        e = "0" + str(pos_t % 60)
    else:
        e = str(pos_t % 60)
    answer = s + ":" + e
    return answer