class Solution:
    """
    Two cases in the while loop to add new elements
    1. When nums[fast] != nums[slow]
    2. Not the start element and count < 2
    We also need a condition to reset count.

    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        slow = fast = 0
        count = 0
        while fast < len(nums):
            # if new element
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            # if not the first element (slow < fast)
            # and the frequency of the element is less than 2
            elif slow != fast and count < 2:
                slow += 1
                # fast is always out to look for the next non-duplicate
                nums[slow] = nums[fast]
            count += 1
            fast += 1 
            if fast < len(nums) and nums[fast - 1] != nums[fast]:
                count = 0
        return slow + 1
