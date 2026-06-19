def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2
    
    def time_angles(t):
        
        h_angle = (t * (1 / 120)) % 360
        m_angle = (t * 0.1) % 360
        s_angle = (t * 6) % 360
        
        return h_angle, m_angle, s_angle
    
    h_angle, m_angle, s_angle = time_angles(start_time)
    if h_angle == s_angle or m_angle == s_angle:
        answer += 1
    
    for t in range(start_time, end_time):
        ch_angle, cm_angle, cs_angle = time_angles(t)
        nh_angle, nm_angle, ns_angle = time_angles(t + 1)
        
        if nh_angle == 0:
            nh_angle = 360
        if nm_angle == 0:
            nm_angle = 360
        if ns_angle == 0:
            ns_angle = 360
            
        if cs_angle < ch_angle and ns_angle >= nh_angle:
            match_hour = True
        else:
            match_hour = False
        if cs_angle < cm_angle and ns_angle >= nm_angle:
            match_min = True
        else:
            match_min = False
        
        if match_hour and match_min:
            if nh_angle == nm_angle:
                answer += 1
            else:
                answer += 2
        elif match_hour or match_min:
            answer += 1

    return answer