from typing import List
class Solution:
    """
    Trick to turn a matrix coordinate into a index, and vice versa: 
    coordinate (i, j) = i * n + j

    i = index // n
    j = index % n
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.convertIndexToMatrix(matrix, mid) == target:
                return True
            elif self.convertIndexToMatrix(matrix, mid) > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
    
    # Convert an index to a specific element in the matrix
    def convertIndexToMatrix(self, matrix, index):
        n = len(matrix[0])
        i = index // n
        j = index % n
        return matrix[i][j]
