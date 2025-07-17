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
                    # All the elements in the same diagonal have the same 
                    # diag value (i - j)
                    lookup[diag] = [mat[i][j]]
                else:
                    lookup[diag].append(mat[i][j])

        # Sort the diagonals
        # Sort the diagonals in descending order because we want to pop
        # the last element in the diagonal first 
        for d in lookup.values():
            d.sort(reverse = True)

        # Fill the matrix with the sorted diagonals 
        for i in range(m):
            for j in range(n):
                diag = i - j
                mat[i][j] = lookup[diag].pop()

        return mat