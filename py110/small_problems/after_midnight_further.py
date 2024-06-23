HOURS_IN_DAY = 24
MINUTES_IN_DAY = 1440
MINUTES_IN_HOUR = 60

WEEK_DAYS = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def time_of_day(minutes):
    day_idx = minutes // MINUTES_IN_DAY
    day = WEEK_DAYS[day_idx]

    leftover_minutes = minutes % MINUTES_IN_DAY
    hours, minutes = divmod(leftover_minutes, MINUTES_IN_HOUR)

    return f"{day}, {hours:02d}:{minutes:02d}"

print(time_of_day(0))# == "00:00")        # True
print(time_of_day(-3))# == "23:57")       # True
print(time_of_day(35))# == "00:35")       # True
print(time_of_day(-1437))
print(time_of_day(3000))# == "00:03")    # True
print(time_of_day(800))# == "13:20")      # True
print(time_of_day(-4231))# == "01:29")    # True