#!/usr/bin/env python

"""Script that checks 1-100 and prints Fizz if a multiple of 3,
Buzz if a multiple of 5 and FizzBuzz if the number is both a multiple of 3 and 5"""

import sys

# To install term color - pip install termcolor
from termcolor import colored, cprint

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        cprint('FizzBuzz', 'red')
    if num % 3 == 0:
        cprint('Fizz', 'blue')
    elif num % 5 == 0:
        cprint('Buzz', 'green')
    else:
        print(num)