
from datetime import datetime

def get_days_from_today(date):
    try:
        datetime_now = datetime.today() # Get today's date
        date_user = str(date) 
        date_user = datetime.strptime(date_user, "%Y.%m.%d") # Parse the date string to a datetime object
        datetime_total = (date_user - datetime_now).days # Calculate the difference in days between the specified date and today's date
        return datetime_total
    except ValueError:
        return "Неверный формат даты. Пожалуйста, укажите дату в формате: ГГГГ.ММ.ДД"

print(get_days_from_today("2021.10.10"))
