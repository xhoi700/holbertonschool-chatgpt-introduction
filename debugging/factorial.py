#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrease n by 1 to avoid infinite loop
    return result

f = factorial(int(sys.argv[1]))  # Convert the argument to an integer and compute the factorial
print(f)
