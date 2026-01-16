def solution(id_pw, db):
    answer = "fail"
    for s in db:
        if s[0] == id_pw[0]:
            if s[1] == id_pw[1]:
                answer = "login"
                break
            answer = "wrong pw"
    return answer