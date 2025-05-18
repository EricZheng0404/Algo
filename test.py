from typing import List

def search(nums:  List[int], target: int):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            r = mid - 1
        else: 
            l = mid + 1
    return -1

print(search([0, 1, 2, 3, 4, 5], 3))
