def solution(id_list, report, k):
    answer = []
    report_dict = {}
    count_dict = {}
    for id in id_list:
        report_dict[id] = set()
        count_dict[id] = 0
    for re in report:
        reporter, reported = re.split()
        report_dict[reporter].add(reported)
    for id in id_list:
        for people in report_dict[id]:
            count_dict[people] += 1
    for id in id_list:
        cnt = 0
        for id_re in report_dict[id]:
            if count_dict[id_re] >= k:
                cnt += 1
        answer.append(cnt)
        cnt = 0
    
    return answer