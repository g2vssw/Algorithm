def solution(N, stages):
    answer = []
    
    # rate_list는 (실패율, 스테이지 번호) 튜플을 담는 리스트
    rate_list = []
    
    # people은 각 스테이지에 도달한 인원수로 처음 전체 인원수(stages1)에서 앞 선 스테이지 인원 수를 빼서 계산
    people = len(stages)
    
    # count_list는 인덱스 활용(스테이지 번호 별 인원 카운트)을 위해 사용
    # stages에는 1 이상 N + 1 이하의 자연수가 담겨있기 때문에 0이 (N + 2)인 배열을 만듬
    count_list = [0] * (N + 2)
    for stage in stages:
        count_list[stage] += 1
    
    # 스테이지의 개수는 N으로 1부터 N까지 스테이지
    for i in range(1, N + 1):
        # 만약 남아 있는 스테이지가 있어도 참가 인원이 없다면 실패율은 0
        if people == 0:
            rate = 0
        else:
            rate = count_list[i] / people
        
        # 해당 스테이지 인원수 만큼 줄어드는 것을 반영
        people -= count_list[i]
        # rate_list에 (실패율, 스테이지 번호) append
        rate_list.append((rate, i))
    
    # 실패율이 높은 스테이지부터 내림차순, 실패율이 같은 경우 작은 번호의 스테이지가 먼저 오도록
    rate_list.sort(key = lambda x: (-x[0], x[1]))
    
    # answer에 스테이지 번호만 순서대로 append
    for rs in rate_list:
        answer.append(rs[1])

    return answer