class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                # Check for rows
                if board[i][j] in rows[i]:
                    return False 
                rows[i].add(board[i][j])
                # Check for cols
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                # Check for block
                blockIndex = i // 3 * 3 + j % 3 # (0, 6)
                if board[i][j] in blocks[blockIndex]:
                    return False
                blocks[blockIndex].add(board[i][j])
        return True
        