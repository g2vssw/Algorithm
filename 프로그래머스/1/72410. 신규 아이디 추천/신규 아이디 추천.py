def solution(new_id):
    answer = ''
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    answer1 = ""
    for s in new_id:
        answer1 += s.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    answer2 = ""
    for s in answer1:
        if s in "~!@#$%^&*()=+[{]}:?,<>/":
            continue
        answer2 += s
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    answer3 = ""
    flag = 0
    for s in answer2:
        if s == ".":
            if flag == 1:
                continue
            else:
                flag = 1
                answer3 += s
        else:
            flag = 0
            answer3 += s     
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    def remove_pe(ans):
        if len(ans) == 0:
            return ans
        if ans[0] == ".":
            ans = ans[1:]
        if len(ans) == 0:
            return ans
        if ans[-1] == ".":
            ans = ans[:-1]
        return ans
    answer4 = remove_pe(answer3)
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(answer4) == 0:
        answer5 = "a"
    else:
        answer5 = answer4
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer5) >= 16:
        answer6 = remove_pe(answer5[:15])
    else:
        answer6 = answer5
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(answer6) <= 2:
        for _ in range(3 - len(answer6)):
            answer6 += answer6[-1]
    answer = answer6
    return answer