# PROBLEM:
#     - Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm).
#     - Your function should work with any integer input.
    
# RULES:
#     - cannot use datetime
#     - positive number is after midnight, negative number is before midnight

# DATA STRUCTURES:
#     - int to store minutes
#     - int to store hours

# ALGORITHM:
#     - work out number of hours of integer input -> hours == int_input // 60
#.    - work out number of minutes of integer input -> divmod(number, 60)

MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

def time_of_day(minutes):
    total_hours = minutes // MINUTES_IN_HOUR
    hours_remaining = total_hours % HOURS_IN_DAY
    minutes_remaining = minutes % MINUTES_IN_HOUR
    
    return f"{hours_remaining:02d}:{minutes_remaining:02d}"




# TEST CASES:
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True