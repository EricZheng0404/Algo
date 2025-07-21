def search_range(nums, target):
    def find_left(nums, target):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else: # nums[mid] >= target
                if nums[mid] == target:
                    res = mid
                right = mid - 1
        return res

    def find_right(nums, target):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid] == target:
                    res = mid
                left = mid + 1
        return res

    left = find_left(nums, target)
    right = find_right(nums, target)
    return [left, right]
nums = [5,7,7,8,8,10]
target = 8
assert search_range(nums, target) == [3, 4]


nums = [5,7,7,8,8,10]
target = 6
assert search_range(nums, target) == [-1, -1]

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def next_greatest_letter(letters, target):
    left, right = 0, len(letters) - 1
    res = letters[0]
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            res = letters[mid]
            right = mid - 1
        else:
            left = mid + 1
    return res

print(max(1, [2,3]))