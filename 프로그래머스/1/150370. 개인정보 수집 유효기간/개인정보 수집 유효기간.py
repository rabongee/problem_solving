def solution(today, terms, privacies):
    answer = []
    
    def compare_day(date):
        year, month, day = map(int, date.split('.'))
        return year * 12 * 28 + month * 28 + day

    today_days = compare_day(today)
    
    term_dict = {} #terms = {t[0]:int(t[2:]) for t in terms}
    for term in terms: 
        term_type, term_num = term.split()
        term_dict[term_type] = int(term_num)

    for i, privacy in enumerate(privacies):
        date_str, term_type = privacy.split()
        expiration_days = compare_day(date_str) + term_dict[term_type] * 28 - 1

        if today_days > expiration_days:
            answer.append(i + 1)

    return answer