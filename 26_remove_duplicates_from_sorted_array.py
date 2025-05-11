"""
LeetCode 26: Remove duplicates from sorted array

Input: 
- A array of integer in non-descending order

Output:
- The number of unique value

Requirement: w
Modify the array in-place with unique values.

The key is to use slow, fast pointer:
[0, slow] is the interval where it's all unique values.
[0, fast] is the interval where it's all traversed values
"""
def removeDuplicate(nums):
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1

