# PROBLEM:
#     - write a program that takes a floating point value and converts it to degrees -> minutes -> seconds
    
# RULES:
#     - degrees minutes and seconds must use appropriate symbol
#     - degree = 60 minutes
#     - minute = 60 seconds

# INPUT:
#     integer

# OUTPUT:
#     formatted string

# DATA STRUCTURES:
#     list to store characters
#     join at the end

# ALGORITHM:
#     - split into int and decimal parts with integer % 1
#     - take int part and add to string
#     - add degree symbol to string
    
#     - take decimal remainder and times by 60 to get minutes
#     - minutes % 1 to get remainder
#     - remainder * 60 to get seconds


DEGREE = "\u00B0"
MINUTE = "'"
SECOND = '"'

def add_zero(num):
    if len(str(int(num))) < 2:
       return '0' + str(int(num))

def dms(num):
    degrees_remainder = num % 1
    degrees = str(int(num - degrees_remainder)) + DEGREE
    
    minutes = degrees_remainder * 60
    minutes_remainder = minutes % 1
    if len(str(int(minutes))) < 2:
        minutes = add_zero(minutes) + MINUTE
    else:
        minutes = str(int(minutes)) + MINUTE
    
    seconds = minutes_remainder * 60
    if len(str(int(seconds))) < 2:
        seconds = add_zero(seconds) + SECOND
    else:
        seconds = str(int(seconds)) + SECOND
    
    return degrees + minutes + seconds
    



# TEST CASES:
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")