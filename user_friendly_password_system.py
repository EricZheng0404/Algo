#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
import string 
M = 10**9 + 7
P = 131
PP = [P ** i for i in range(11)]
APPENDS = [""] + list(string.ascii_letters) + [str(i) for i in range(10)]



def calc(pw):
    result = 0
    for i in range(len(pw)):
        result += ord(pw[-(i+1)]) * PP[i]
    return result%M
    
            
def authEvents(events):
    currPassword = set() 
    result = []
    for action, param in events:
        if action == "setPassword":
            currPassword.clear()
            for i in APPENDS:
                currPassword.add(calc(param + i))
    
        else:
            if int(param) in currPassword:
                result.append(1)
            else:
                result.append(0)
    return result
        
def test_auth_events():
    # Test Case 1: Basic password set and auth
    events1 = [
        ["setPassword", "cAr1"],
        ["authorize", str(calc("cAr1"))]
    ]
    assert authEvents(events1) == [1], "Test Case 1 failed"

    # Test Case 2: Multiple password sets
    events2 = [
        ["setPassword", "cAr1"],
        ["authorize", str(calc("cAr1"))],
        ["setPassword", "cAr2"],
        ["authorize", str(calc("cAr1"))]
    ]
    assert authEvents(events2) == [1, 0], "Test Case 2 failed"

    # Test Case 3: Empty password
    events3 = [
        ["setPassword", ""],
        ["authorize", str(calc(""))]
    ]
    assert authEvents(events3) == [1], "Test Case 3 failed"

    # Test Case 4: Single character
    events4 = [
        ["setPassword", "a"],
        ["authorize", str(calc("a"))]
    ]
    assert authEvents(events4) == [1], "Test Case 4 failed"

    # Test Case 5: Multiple authorize attempts
    events5 = [
        ["setPassword", "test123"],
        ["authorize", str(calc("test123"))],
        ["authorize", str(calc("test123") + 1)]
    ]
    result5 = authEvents(events5)
    assert len(result5) == 2, "Test Case 5 failed - wrong number of results"
    assert result5[0] == 1, "Test Case 5 failed - first auth should succeed"
    assert result5[1] == 0, "Test Case 5 failed - second auth should fail"


    events6 = [
        ["setPassword", "cAr1"],
        ["authorize", str(223691457)],
        ["authorize", str(303580761)],
        ["authorize", str(100)],
        ["setPassword", "d"],
        ["authorize", str(100)]
    ]
    result6 = authEvents(events6)
    assert result6 == [1, 1, 0, 1], "Test Case 6 failed - wrong results"

    print("All test cases passed!")

if __name__ == "__main__":
    test_auth_events()  
