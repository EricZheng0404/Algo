class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.path = []
        self.n = len(nums)
        self.used = [False] * self.n
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums):
        # The end condition: when all nums are added to self.path at the end of
        # the path.
        if len(self.path) == self.n: # I set this to self.path instead of len(self.path)
            self.res.append(self.path[:])
            return
        for i in range(self.n):
            # We don't want any used choices. We can handle this in here
            if self.used[i] == True:
                continue
            # Make a choice
            self.used[i] = True # I used == 
            self.path.append(nums[i])
            # Enter the next level of the decision tree
            self.backtrack(nums)
            # Undo the choice
            self.used[i] = False # I used ==
            self.path.pop()