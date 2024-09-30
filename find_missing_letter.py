"""
PROBLEM:
From a given string, return whether the parentheses are valid.

Parentheses are valid when:
- there is an even number of them -> '()' not '()('
- The first parentheses is open -> '()' not ')()'
- closed and open are equal -> '()()' not '()))'
- ends in closed parenthesis -> '()))((())'
- the opening bracket is an odd number of indexes away from the closing bracket -> '() 

Maybe need to track pairs and make sure they close

Hsie -100
Hed s 0
B 
b si -17
v po -26
h an 11
h po 0
v ang 51
poin 8
shap 100
wei 100
A bul 100
Ni circ 100
Ni pro 100
Ae si 100
Ni type a bot

B sca 74
B sca2 74
B sca3 100
E b sca1 115

Ni sca 115
ni ti sca 85

Nec W -29
Nec Th -26
Sh W -34
sh Th 19
U Tor W -31
U Tor Th -9
L Tor W -25
L Tor Th -39

U Tor sca 88
Mi Tor sca 91
spin cur 2 10
L Tor sca 88
spin cur 1 10

Wai pos 64
stom 9
U hi w 15
u hi th 3
Low hi w 0
Low hi th 37
Bt si 51
Bt ang 94
as pos 167

U wai sca 83
L wai sca 80
W L sca1 94
W L sca2 73

rms
-40
-46
-47
-17
-16
-17
-57

rms2
85
103

hnd
h sca1 74
"""

"""
PROBLEM:
return an integer representing total seconds as human readable time in hours, minutes, and seconds -> HH:MM:SS

INPUT:
integer (seconds)

OUTPUT:
string ("HH:MM:SS")

EXAMPLE:
make_readable(0) "00:00:00"
make_readable(59) "00:00:59"
make_readable(60) "00:01:00"
make_readable(3599) "00:59:59"
make_readable(3600) "01:00:00"
make_readable(86400) "24:00:00"
make_readable(359999) "99:59:59"

ALGORITHIM:

work out total hours in time using divmod to store the remainder -> hours, remainder = divmod(input, 3600)
work out total minutes with remainder -> minutes, remainder = divmod(remainder, 60)
seconds is equal to the remainder -> seconds = remainder
return a string consisting of hours, minutes and seconds


"""
"""
PROBLEM:
work out how many times the mother will see the ball.
the ball bounces two-thirds of it's height
the mother is looking out a window 1.5m from the ground

Rules:
The ball can only be seen if it is strictly greater than the window parameter

ALGORITHIM:
work out if the experiment is valid: if not, return -1
the mother will see the ball when it is first dropped, so seen = 1
the ball when then bounce up a distance of height * bounce, height should be reset to bounce * height
if this bounce height is greater than window height, seen += 1 else return seen
"""
def bouncing_ball(h, bounce, window):
    if h <= 0 or 0 >= bounce >= 1 or window >= h:
        return -1

    seen = 0

    while h > window:
        h *= bounce
        if h > window:
            seen += 2
        else:
            seen += 1

    return seen

print(bouncing_ball(30, 0.75, 1.5))
# height is 3, 1.98
# bounce is 0.66
# window is 1.5
    