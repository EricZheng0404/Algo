"""
LeetCode 88: merge two arrays

Modify num1 in-place(!!!) using slice assignment. 
"""

class Solution(object):
    # Implementation1: Use extra list reulst 
    def merge1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        result = []
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
        if p1 < m:
            result.extend(nums1[p1:m])
        if p2 < n:
            result.extend(nums2[p2:n])
        nums1[:len(result)] = result

    # In-place without using 
    def merge2(self, nums1, m, nums2, n):
        p1, p2 = m - 1, n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else: 
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol = Solution()
    # # Implementation 1
    # sol.merge1(nums1, m, nums2, n)
    # print(nums1)
    sol.merge2(nums1, m, nums2, n)
    print(nums1)

