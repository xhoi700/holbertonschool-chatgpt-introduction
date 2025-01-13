#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Redukto vlerën e n për të shmangur një loop të pafund
    return result

f = factorial(int(sys.argv[1]))
print(f)
