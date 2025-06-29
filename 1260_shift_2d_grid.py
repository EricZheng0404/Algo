class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 1. Convert the grid to a 1D array
        arr = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
        # 2. Shift k times
        newK = k % (m * n)
        self.reverse(arr, 0, m * n - 1)
        self.reverse(arr, 0, newK - 1)
        # print(arr)
        self.reverse(arr, newK , m * n - 1)
        # print(arr)
        # 3. Convert back to a 2D grid
        res = [[0] * n for _ in range(m)]
        numIndex = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = arr[numIndex]
                numIndex += 1
        return res

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1