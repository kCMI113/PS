def date_to_days(date):
    year, month, day = map(int, date.split("."))
    return day + month*28 + year*12*28
    
def solution(today, terms, privacies):
    terms_days = {ele[0]:int(ele[2:])*28 for ele in terms}
    
    today_days = date_to_days(today)
    answer = [ i for i, privacy in enumerate(privacies, start=1) if (date_to_days(privacy[:-2]) + terms_days[privacy[-1]]) <= today_days]

    return answer