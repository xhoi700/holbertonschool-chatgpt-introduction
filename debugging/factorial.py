#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Zvogëlojmë vlerën e n pas çdo iteracioni
    return result

if len(sys.argv) < 2:
    print("Ju lutem jepni një numër si argument.")
    sys.exit(1)

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Ju lutem jepni një numër të vlefshëm.")
    sys.exit(1)
