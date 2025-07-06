class Solution:
    """
    1. The window has k elements, the next elements is the (k+1)th elmeent, so overall 
    (i - j) = k.
    2. To find if we can find abs(nums[i] - nums[j]), we first use SortedList to find 
    the closest element to the elem in the list, and then check if their diff is less
    than or equal to valueDiff.
    """
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedList
        window = SortedList()
        for i in range(len(nums)):
            # figure out the position of the element in the list
            pos = window.bisect_left(nums[i])
            # If the position of the element is in the window
            if len(window) > 0 and pos < len(window) and abs(window[pos] - nums[i]) <= valueDiff:
                return True
            # If the position of the element is at the last of the window
            if pos > 0 and abs(nums[i] - window[pos - 1]) <= valueDiff:
                return True

            # Expand Window
            window.add(nums[i]) # It's add

            # Shrink window
            if len(window) > indexDiff:
                # We should remove the first element
                window.remove(nums[i - indexDiff])
        return False
