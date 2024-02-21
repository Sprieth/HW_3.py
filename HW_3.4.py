
from datetime import datetime, timedelta

users = [
    {"name": "Max", "birthday": "2000.02.23"},
    {"name": "Alexandr", "birthday": "1999.11.20"},
    {"name": "Vlad", "birthday": "1998.02.28"}
]

def get_upcoming_birthdays(users):
    date_today = datetime.today().date() # Вказує сьогоднішню дату
    upcoming_birthdays = []

    for user in users: # Цикл який аналізуйте дати народження кожного користувача
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # Вказує дату дня народження користувача
        birthday_this_year = birthday.replace(year=date_today.year) 

        if birthday_this_year < date_today: # Перевіряє, чи вже минув день народження в цьому році
            birthday_this_year = birthday_this_year.replace(year=date_today.year + 1)


        days_until_birthday = (birthday_this_year - date_today).days # Рахуэ  дні до дня народження

        if 0 <= days_until_birthday <= 7: # Перевіряє, різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5: # Перевіряє, чи день народження припадає на вихідний
                days_until_monday = (7 - congratulation_date.weekday()) % 7
                congratulation_date += timedelta(days=days_until_monday)


            upcoming_birthdays.append({ 
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


upcoming = get_upcoming_birthdays(users)
for user in upcoming:
    print(f"{user['name']} - {user['congratulation_date']}")