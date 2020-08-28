import datetime
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

birth_year, birth_month, birth_day = map(int, input('생년월일 입력: ').split())
birth_year, birth_month, birth_day

if birth_month < current_month:         #현재 월 > 생월
    age = current_year - birth_year
elif birth_month > current_month:       #현재 월 < 생월
    age = current_year - birth_year - 1
else:                                   #현재 월 == 생월
    if birth_day > current_day:         #현재 일 < 생일
        age = current_year - birth_year - 1
    else:                               #현재 일 >= 생일
        age = current_year - birth_year

print('만 나이는 %d 입니다.' % age)