#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("No arguments were provided.")
else:
    for i in range(1, len(sys.argv)):  # Start from 1 to skip the script name
        print(sys.argv[i])
