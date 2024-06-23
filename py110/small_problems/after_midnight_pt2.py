MINUTES_IN_DAY = 1440
HOUR_MINUTES = 60
DAY_HOURS = 24

def after_midnight(minutes_hours):
    hours = int(minutes_hours[:2]) % DAY_HOURS
    minutes = int(minutes_hours[3:])
    
    return (hours * HOUR_MINUTES) + minutes
    
def before_midnight(minutes_hours):
    hours = int(minutes_hours[:2]) % DAY_HOURS
    minutes = int(minutes_hours[3:])
    
    return (((hours * HOUR_MINUTES) + minutes) if hours % 24 == 0
             else abs(((hours * HOUR_MINUTES) + minutes) - MINUTES_IN_DAY))
    
#print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00"))# == 0)    # True
#print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34"))# == 686)  # True
#print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00"))# == 0)    # True