from datetime import datetime, timedelta

day_of_birth = [{"name":"Bill", "birthday":"2002-05-21"},
        {"name":"Kim", "birthday":"1980-05-20"},
        {"name":"Jill", "birthday":"1998-05-22"},
        {"name":"Jan", "birthday":"1976-05-27"}]

days_name = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
    }

def get_birthdays_per_week(users: list) -> str: 

    birth_in_this_year = {}
    day_now = datetime.now().date()

    for inform in users:
        birth = inform.get("birthday")
        name = inform.get("name")

        birthday = datetime.strptime(birth, '%Y-%m-%d').date()
        year_now_date = birthday.replace(day_now.year)
        day_of_week = days_name.get(year_now_date.weekday())

        time_diff = year_now_date - day_now
        str_time_diff = time_diff.days

        if str_time_diff >= 1 and str_time_diff < 5:
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                if birth_in_this_year.get('Monday'):
                    birth_in_this_year['Monday'].append(name)
                else:
                    birth_in_this_year['Monday'] = [name]
            else:
                if birth_in_this_year.get(day_of_week):
                    birth_in_this_year[day_of_week].append(name)
                else:
                    birth_in_this_year[day_of_week] = [name]

    for day_of_week, name in birth_in_this_year.items():
        birthdays = f'{day_of_week}: {", ".join(name)}'    
        
    return birthdays
    
print(get_birthdays_per_week(day_of_birth))