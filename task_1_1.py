""" 1. Реализовать вывод информации о промежутке времени в
зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
** до месяца, до года, больше года: по аналогии.

"""

time = [45, 189, 3795, 11874, 14689, 20234, 90000, 145865]
one_minute = 60
one_hour = 3600
one_day = 86400

for duration in time:
    if duration < one_minute:
        print(duration, 'sec')
    elif one_minute < duration < one_hour:
        minutes = duration // one_minute
        seconds = duration % one_minute
        print(minutes, 'min', seconds, 'sec')
    elif one_minute < duration >= one_hour and duration < one_hour * 24:
        hours = duration // one_hour
        minutes = duration % one_hour // one_minute
        seconds = duration % one_minute
        print(hours, 'hour', minutes, 'min', seconds, 'sec')
    elif one_hour < duration:
        days = duration // one_hour // 24
        hours = duration % one_day // one_hour
        minutes = duration % one_hour // one_minute
        seconds = duration % one_minute
        print(days, 'day', hours, 'hour', minutes, 'min', seconds, 'sec')
