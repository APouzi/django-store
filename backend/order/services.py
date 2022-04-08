from datetime import date
from random import randint

def trackingNumberGenerator():
    test = date.today().isocalendar() #Week meaning the week of the year
    weekYearRandNum = str(test.week) + str(test.year % 100) + str(randint(100000, 9998999))
    
    return weekYearRandNum

