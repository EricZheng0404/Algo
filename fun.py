nums1 = [1, 2, 3, 0, 0, 0]
print(nums1)
pointer = nums1
result = [1, 2, 3, 4, 5, 6]

# This modifies nums1 IN-PLACE
nums1[:] = result

print("nums1: ", nums1)  # Output: [1, 2, 3, 4, 5, 6]
print("pointer: ", pointer)