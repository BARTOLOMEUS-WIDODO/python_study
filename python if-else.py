#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 == 1: # if n is odd
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5: # If n is even and in the inclusive range of 2 to 5
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20: #if n is even and greater than 20
    print("Not Weird")

