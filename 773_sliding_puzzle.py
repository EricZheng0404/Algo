from collections import deque
from typing import List

"""

"""
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"
        # Board processing
        start = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        
        # Intialization
        visited = set()
        visited.add(start)
        q = deque()
        # I started using deque(start), and deque treated start as a iterable
        q.append(start)
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                currBoard = q.popleft()
                # print("currboard", currBoard)
                if currBoard == target:
                    return step
                for neighborBoard in self.getNeighborBoards(currBoard):
                    # We don't want to reverse to the previous board
                    if neighborBoard not in visited:
                        visited.add(neighborBoard)
                        q.append(neighborBoard)
            step += 1
        return -1

    def getNeighborBoards(self, board):
        mapping = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        indexOfZero = board.index('0')
        res = []
        for possibleIndex in mapping[indexOfZero]:
            res.append(self.swapping(possibleIndex, indexOfZero, board))
        return res
            
    def swapping(self, i, j, board):
        letters = list(board)
        letters[i], letters[j] = letters[j], letters[i]
        return "".join(letters)
