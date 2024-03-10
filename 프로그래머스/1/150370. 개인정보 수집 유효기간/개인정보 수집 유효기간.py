
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
def solution(today, terms, privacies):
    answer = []
    terms_dict = {ele.split()[0]:int(ele.split()[1]) for ele in terms}
    days = [i for i in range(1,29)] 

    now_year, now_month, now_day = map(int, today.split("."))

    for i, privacy in enumerate(privacies, start=1):
        p_year, p_month, p_day_term = privacy.split(".")
        p_term = p_day_term[-1]
        p_day = int(p_day_term[:2])
        p_term = terms_dict[p_term]

        pred_month = (int(p_month) + p_term%12)%12 - (p_day==1)
        if pred_month <= 0:
            pred_month += 12

        pred_year = int(p_year) + p_term//12 + ((int(p_month) + p_term%12) > 12)
        pred_day = days[p_day-2]

        if pred_year < now_year:
            answer.append(i)
            continue
        if pred_year == now_year and pred_month < now_month:
            answer.append(i)
            continue
        if pred_year == now_year and pred_month == now_month and pred_day < now_day:
            answer.append(i)

    return answer