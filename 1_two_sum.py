"""
Given a sorted array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Note:
You may assume that each input would have exactly one solution and you may not use the same element twice.
"""
def twoSum(nums, target):
    res = {}
    for i in range(len(nums)):
        # When we encounter a new number, we first calculate the complement we want.
        # Say we have the number 2, that the complement that makes the target is (9-2)=7
        complement = target - nums[i] 
        # If the complement is in the result, we return the index of the current 
        # number and the complement's index
        if  complement in res: 
            return [i, res[complement]]
        # If we can't find the complement, we store the current number and its index
        # so that it can be found later as complement
        res[nums[i]] = i
    # A safeguard. Not really necessary, but just here that we have something to return
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 5]
    target = 9
    print(twoSum(nums, target))