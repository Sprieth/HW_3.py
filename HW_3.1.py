
from datetime import datetime

def get_days_from_today(date):
    datetime_now = datetime.today() # Вказуе сьогоднішню дату
    date_user = str(date) 
    date_user = datetime.strptime(date_user, "%Y.%m.%d") # Виводить дату в форматі datatime

    datetime_total = (date_user - datetime_now).days
    datetime_total = datetime_total
    return datetime_total

print(get_days_from_today("2021.10.10"))

