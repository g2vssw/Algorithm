def t_day(date):
    y, m, d = map(int, date.split("."))
    return (y * 12 * 28) + (m * 28) + d

def solution(today, terms, privacies):
    answer = []
    todays = t_day(today)
    terms_dict = {}
    for term in terms:
        t, month = term.split()
        terms_dict[t] = int(month)
        
    for i in range(len(privacies)):
        date, term_type = privacies[i].split()
        privacy_days = t_day(date)
        
        expire_days = privacy_days + (terms_dict[term_type] * 28)
        
        if todays >= expire_days:
            answer.append(i + 1)
    return answer