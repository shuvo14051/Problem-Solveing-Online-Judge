#!/bin/python3
"""
It give me 16.0 out of 20.0
"""
import math
import os
import random
import re
import sys


def solve(s):
    return s.title()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
