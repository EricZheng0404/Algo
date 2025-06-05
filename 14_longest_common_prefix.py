class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs[0]:
            return res
        m = len(strs[0]) # col
        n = len(strs) # row
        if n == 1:
            return strs[0]
        
        for col in range(m):
            char = strs[0][col]
            for row in range(1, n):
                # In case the length of the first string is longer than other strings
                if col >= len(strs[row]) or char != strs[row][col]:
                    return strs[0][:col]
                    # return strs[row][:col] # We should return [:col] here because it's [left, right)
        return strs[0]

        