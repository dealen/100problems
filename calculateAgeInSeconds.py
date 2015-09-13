from calendar import isleap
from datetime import datetime
from datetime import date

__author__ = 'dealen'


def convert(birth_day, birth_month, birth_year):
    result = 0.0
    start_year = birth_year
    days_in_birth_year = (date(birth_year, 1, 1) - date(birth_year, birth_month, birth_day)).days
    days_in_current_year = (date(datetime.now().year, datetime.now().month, datetime.now().day) -
                            date(datetime.now().year, 1, 1)).days

    while start_year < datetime.now().year:
        if isleap(birth_year):
            days_in_year = 366.0
        else:
            days_in_year = 365.0

        if start_year == birth_year:
            days_in_year += days_in_birth_year
        elif start_year == datetime.now().year:
            days_in_year += days_in_current_year

        result += 24.00*3600.00*days_in_year
        start_year += 1
    return result

print('Age in seconds calculator.')
year_of_birth = int(input('Enter year of your birth :'))
month_of_birth = int(input('Enter month of your birth :'))
day_of_birth = int(input('Enter day of your birth :'))
print('Your age equals ', str(convert(day_of_birth, month_of_birth, year_of_birth)), ' seconds')
