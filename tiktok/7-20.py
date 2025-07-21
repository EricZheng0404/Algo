"""
Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where 
each string is a suit in Stark's collection, count the total number of unique 
suits in the list.
"""
def count_suits_recursive(suits):
    if not suits:
        return 0
    suitSet = set()
    return helper(suits, suitSet)

def helper(suits, suitSet):
    # Tail recursion: the recursive call is the last statement in the function
    if not suits:
        return len(suitSet) # We only return when we hit base case
    suitSet.add(suits[0])
    # All other recursive calls returns whatever their recursive call returns
    return helper(suits[1:], suitSet) 


"""
Problem 4: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where 
each string is a suit in Stark's collection, count the total number of unique 
suits in the list.

16
Example 1 Explanation: 2 to the 4th power (4 * 4) is 16. 
0.0625
Example 2 Explanation: -2 to the 4th power is 1/(4 * 4) is 0.0625.
"""

def power_of_four(n):
    if n == 0:
        return 1
    if n > 0:
        return 4 * power_of_four(n - 1)
    elif n < 0: 
        print(f"power_of_four(-n): {power_of_four(-n)}")
        return 1 / (power_of_four(-n))

print(power_of_four(2))
print(power_of_four(-2))

"""
Problem 6: Strongest Avenger
The Avengers need to determine who is the strongest. Given a list of their 
strengths, find the maximum strength using a recursive approach without using 
the max() function.
"""

def strongest_avenger(strengths):
    """
    Base case: when there's only one element in the list, return that element
    Recursive case: return the max of the first element and the rest of the list
    """
    if len(strengths) == 1:
        return strengths[0]
    # strongest_avenger(strengths[1:]) is the result of the recursive call,
    # which is a number
    return max(strengths[0], strongest_avenger(strengths[1:]))
