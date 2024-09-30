""" 
PROBLEM:
Write a function that takes two integer arguments (n and m) and returns 
a sorted list of all the integers that have 3 divisors from n to m inclusive, excluding 1 and the number itself.

EXAMPLE:
2 -> None
3 -> None
4 -> 2
5 -> None
6 -> 2, 3
7 -> None
8 -> 2, 4
9 -> 3
10 -> 2, 5
11 -> None
12 -> 2, 6
13 -> None
14 -> 2, 7
15 -> 3, 5
16 -> 2, 8, 4
17 -> None
18 -> 2, 9, 3, 6
19 -> None
20 -> 2, 10, 4, 5


ALGORITHIM: 1420
FIND PRIMES
1. take integer -> 9
2. assign numbers from 2 to number - 1 to a dictionary as keys with value None
3. check if numbers in the dictionary keys go into the integer
4. if the numbers go into the number change to False
5. if the numbers don't go into the number change the values to True

FIND PRIME FACTORS
1. divide by least prime number -> 2
2. check if number is divisible by 2 -> 710
    if not divisible by 2, move onto next prime number (3)
3. repeat steps 1 to 2 until a prime number is reached

FIND MULTIPLES OF PRIME FACTORS
1. When a prime number is reached, find all the multiples of the prime factors
"""
9
def generate_primes(number):
    primes = {number: True for number in range(2, number)}
    
    for number in primes:
        for value in range(2, number):
            if number % value == 0:
                primes[number] = False

    return [number for number in primes if primes[number] == True]

def find_primes(number):
    prime_factors = generate_primes(number)
    products_and_primes = [1, number]
    checked_number = number
    idx = 0

    while checked_number not in prime_factors:
        if checked_number % prime_factors[idx] == 0:
            products_and_primes.extend([prime_factors[idx], checked_number // prime_factors[idx]])
            checked_number = checked_number // prime_factors[idx]
        else:
            idx += 1

    return products_and_primes

def find_multiples(lst):
    pass

print(find_primes(210))