# PROBLEM:
#     Write a program that asks for 6 numbers from the user.
#     The program determines if the 6th number is in the first five numbers.
    
# Rules:
#     program must take 6 numbers
#     if a non-integer is given, ask again for a number until valid

# INPUT:
#     integers received from user

# OUTPUT:
#     string saying if 6th number is in first 5

# EXAMPLES:
#     1, 2, 3, 4, 5, 5 -> 5 is in 1, 2, 3, 4, 5

# ALGORITHM:
#     GET values:
#         1. ask for user input
#         2. if input is not an integer
#         3. ask again
#         4. append input to a list
#         repeat until 5 values are collected
        
#     GET comparison value:
#         1. ask again for input
#         2. if input is not an integer
#         3. ask again
#         4. assign comparison value to a variable
    
#     Check comparison:
#         1. determine if comparison value is in value_list
#             - if not in list -> return comparison value is not in value_list
#             - if in list -> return comparison value is in value_list

ordinal_numbers = {0: '1st', 1: '2nd', 2: '3rd', 3: '4th', 4: '5th'}
num_list = []

def value_is_valid(string):
    try:
        int(string)
    except ValueError:
        return False
    return True

def get_values():
    counter = 0
    
    while counter < 5:
        num_list.append(input(f"Enter the {ordinal_numbers[counter]} number: "))
        while value_is_valid(num_list[counter]) == False:
            print("That is not a valid digit!")
            num_list[counter] = input(f"Enter the {ordinal_numbers[counter]} number: ")
        counter += 1

def get_comparison():
    comparison_value = input("Enter a value to compare: ")
    while value_is_valid(comparison_value) == False:
        print("That is not a valid digit!")
        comparison_value = input("Enter a value to compare: ")
    
    return comparison_value
    
def check_numbers(comparison_value):
    
    if comparison_value in num_list:
        print(f"{comparison_value} is in {', '.join(num_list)}")
    else:
        print(f"{comparison_value} is not in {', '.join(num_list)}.")

def main():
    get_values()
    comparison_value = get_comparison()
    check_numbers(comparison_value)

main()
    
    
    