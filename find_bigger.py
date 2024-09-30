"""
PROBLEM:
Write a function that takes an integer as an argument and returns the same digits rearranged to form the next biggest number.

The next biggest number examples:
235 -> 253
1879 -> 1897
308697 -> 308967

loop through number in reverse -> 2017 -> 7102
if the current number is bigger than the next number, swap them
return the number reversed
"""

def next_bigger(n):
    num_list = list(str(n))
    num_list.reverse()
    print(num_list)
    
    for i, num in enumerate(num_list):
        try:
            first = num
            second = num_list[i + 1]
        except IndexError:
            return -1

        if first > second:
            num_list[i] = second
            num_list[i + 1] = first
            num_list.reverse()
    
    return ''.join(num_list)


    
    

print(next_bigger(2488776555)), #   2545567788
#