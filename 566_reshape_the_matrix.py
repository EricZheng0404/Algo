from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat
        res = [[0] * c for _ in range(r)]
        index = 0
        for row in range(r):
            for col in range(c):
                res[row][col] = self.convertIndexToMatrix(mat, index)
                index += 1
        return res

    def convertIndexToMatrix(self, matrix, index):
        n = len(matrix[0])
        i, j = divmod(index, n)
        return matrix[i][j]