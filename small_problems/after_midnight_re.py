# PROBLEM:
#     - write a program that returns the time in hours and minutes (hh:mm) from the amount of minutes after or before midnight

# RULES:
#     - the input integer can be either positive or negative
#     - positive is after midnight
#     - negative is before midnight

# INPUT:
#     - int

# OUTPUT:
#     - string -> "00:00", "23:57"

# ALGORITHM:
#     - work out how many hours are contained in input integer
#         - 3000 input minutes -> 3000 / 60 == 50 hours (0 mins left over)
#         - 800 input minutes -> 800 / 60 == 13 hours (20 mins left over)
#         - 35 input minutes -> 35 / 60 == 0 hours (35 mins left over)
#         - -1437 input minutes -> -1437 / 60 == -23 hours (-57 mins left over)
#         - -4231 input minutes -> -4231 / 60 == -70 hours (-31 mins left over)
    
#     - work out how many days are in that amount of hours, if any, to find leftover hours
#         - 50 hours -> 50 / 24 == 2 with 2 hours left over
#         - 13 hours -> 13 / 24 == 0 (20 mins remaining)
#         - 0 hours -> 0 / 24 == 0 (35 mins remaining)
#         - -23 hours -> -23 / 24 == 0 (-57 mins remaining)
#         - -70 hours -> -70 / 24 == 2days -22 hours left over (-31 mins remaining)
        
#     - work out time after midnight with those leftover hours and minutes
#         - midnight is 00:00. 00:00 plus remaining 2 hours -> 02:00
#         - mindight is 00:00. 00:00 plus remaining 13 hours and 20 minutes -> 13:20
#         - mindight is 00:00. 00:00 plus remaining 0 hours and 35 minutes -> 00:35
#         - mindight is 00:00. 00:00 plus remaining -23 hours and -57 minutes -> 00:03
#         - mindight is 00:00. 00:00 plus remaining -22 hours and -31 minutes -> 01:29
#             - if number of hours and minutes is minus
#                 - for hours + 23 hours -> -23 + 23 == 0
#                 - for minutes + 60 onto minutes -> -57 + 60 == 3
    
HOUR_MINUTES = 60
DAY_MINUTES = 1440

def time_of_day(minutes):
    leftover_minutes = minutes % DAY_MINUTES
    hours, minutes = divmod(leftover_minutes, HOUR_MINUTES)

    return f"{hours:02d}:{minutes:02d}"

# time_of_day(minutes)
# TEST CASES:
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True