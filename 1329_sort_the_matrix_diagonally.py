from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        lookup = {}
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                diag = i - j
                if diag not in lookup:
                    lookup[diag] = [mat[i][j]]
                else:
                    lookup[diag].append(mat[i][j])
        for d in lookup.values():
            d.sort(reverse = True)

        for i in range(m):
            for j in range(n):
                diag = i - j
                mat[i][j] = lookup[diag].pop()

        return mat