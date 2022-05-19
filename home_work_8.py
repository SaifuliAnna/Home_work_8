from datetime import datetime, timedelta

day_of_birth = [
    {"name": "Bill", "birthday": "2002-05-22"},
    {"name": "Kim", "birthday": "1980-05-21"},
    {"name": "Jill", "birthday": "1998-05-19"},
    {"name": "Jan", "birthday": "1976-05-18"},
    {"name": "Dan", "birthday": "1976-05-20"},
    {"name":"Bayden", "birthday":"2002-05-24"},
    {"name":"Kate", "birthday":"1980-05-27"},
    {"name":"Juliya", "birthday":"1998-05-28"},
    {"name":"Jaff", "birthday":"1976-05-27"},
    {"name":"Daniil", "birthday":"1976-05-29"}
]

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_birthdays_per_week(users: list) -> str:
    birth_in_this_year = {}
    start_period = ((datetime.now() - timedelta(days=datetime.now().weekday()) + timedelta(days=5))).date()
    end_period = start_period + timedelta(days=6)

    for inform in users:
        birth = inform. get("birthday")
        name = inform.get("name")

        birthday = datetime.strptime(birth, "%Y-%m-%d").date()
        year_now_date = birthday.replace(start_period.year)

        if start_period <= year_now_date <= end_period:
            day_of_week = days_name.get(year_now_date.weekday())
            if year_now_date.weekday() in (5, 6):
                if birth_in_this_year.get("Monday"):
                    birth_in_this_year["Monday"].append(name)
                else:
                    birth_in_this_year["Monday"] = [name]
            else:
                if birth_in_this_year.get(day_of_week):
                    birth_in_this_year[day_of_week].append(name)
                else:
                    birth_in_this_year[day_of_week] = [name]
    birthdays = ""
    for day_of_week, name in birth_in_this_year.items():
        birthdays += f'{day_of_week}: {", ".join(name)} \n'

    return birthdays
    
print(get_birthdays_per_week(day_of_birth))
