"""
Write a function that returns the angle in degrees, minutes and seconds from a float value

1 degree = 60 minutes
1 minute = 60 seconds
"""
DEGREE = "\u00B0"

def dms(num):
    normalised_num = num % 360

    degrees = normalised_num
    minutes = (normalised_num % 1) * 60
    seconds = (minutes % 1) * 60
    return f'{int(degrees)}{DEGREE}{int(minutes):02}\'{int(seconds):02}"'

print(dms(76.73) == "76°43'48\"")
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"