from calendar import isleap
from datetime import datetime

__author__ = 'dealen'


def convert(age):
    birth_year = datetime.now().year - age
    result = 0.0
    while birth_year < datetime.now().year:
        if isleap(birth_year):
            year_value = 366.0
        else:
            year_value = 365.0
        result += 24.00*3600.00*year_value
        birth_year += 1
    return result

print('Age in seconds calculator.')
age_value = float(input('Enter your age :'))
print('Your age equals ', str(convert(age_value)), ' seconds')
