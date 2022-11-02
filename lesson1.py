birth_year1 = int(input('enter year of birth1: '))
birth_month1 = int(input('enter month of birth1: '))
birth_day1 = int(input('enter date of birth1: '))
birth_year2 = int(input('enter year of birth2: '))
birth_month2 = int(input('enter month of birth2: '))
birth_day2 = int(input('enter date of birth2: '))
year_now = int(input('enter the current year: '))
month_now = int(input('enter the current month: '))
day_now = int(input('enter the current day: '))
full_years1 = (((year_now- birth_year1)*12+(month_now-birth_month1))//12*30+(day_now-birth_day1))//30
full_years2 = (((year_now- birth_year2)*12+(month_now-birth_month2))//12*30+(day_now-birth_day2))//30
if full_year1>full_year2:
    print('The first man is older')
elif full_year1==full_year2:
    print('These people have the same age')
else:
    print('The second man is older')