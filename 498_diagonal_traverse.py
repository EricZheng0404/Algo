from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        index = [[] for _ in range(m + n - 1)]
        for i in range(m):
            for j in range(n):
                index[i + j].append(mat[i][j])
        res = []
        reverse = False
        for lst in index:
            if reverse is True:
                res.extend(lst)
            else:
                lst.reverse()
                res.extend(lst)
            reverse = not reverse
        return res