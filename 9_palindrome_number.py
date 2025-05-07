"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
def isPalidrom(x):
    if x < 0:
            return False
    temp = x
    y = 0
    while temp > 0:
        last_digit = temp % 10 # Get the last digit
        temp = temp // 10 # Update temp by getting rid of the last digit
        y = y * 10 + last_digit # The previous number becomes ten times larger
    return y == x

def isPalidrom2(x):
     num = str(x)
     if num[0] == '-':
          return False
     return num[::1] == num[::-1]