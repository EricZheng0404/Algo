#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'two_sum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER target
#

def two_sum(numbers, target):
    # Write your code here
    l, r = 0, len(numbers) - 1
    while l < r:
        sum_ = numbers[l] + numbers[r]
        if sum_ == target:
            return [l, r]
        elif sum_ < target:
            l += 1
        else: 
            r -=1 
    return [l, r]

print(two_sum([2, 7, 11, 15], 9))