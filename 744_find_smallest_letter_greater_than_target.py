class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # we want close left bound, so we should shrink the right 
            if letters[mid] > target:
                r = mid - 1
            # We want to continue find the letter greater than the mid
            elif letters[mid] == target:
                l = mid + 1
            # In the right range, we should continue with shrink left
            elif letters[mid] < target:
                l = mid + 1
        """
        If target is greater than all the elemnts is the letters, the l will point to
        len(lettters). In this case, we need to manually check this in the final return.
        """ 
        return letters[l] if l < len(letters) else letters[0]