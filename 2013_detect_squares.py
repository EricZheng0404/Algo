from typing import List
from collections import defaultdict
class DetectSquares:

    def __init__(self):
        # point (x, y): frequency (integer number)
        self.points = defaultdict(int)
        # x : [y1, y2, y3, ...]
        self.xMap = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.xMap[x].append(y)

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self.xMap:
            return 0
        # To find all points that's perpendicular to the given point
        count = 0
        # The repetition of the first point is covered because duplicates
        # will be stored in the list
        for ny in self.xMap[x]:
            # The area of the square is more than 0
            if ny == y:
                continue
            sideLength = abs(ny - y)
            for nx in [x + sideLength, x - sideLength]:
                count += (self.points[(nx, y)] * self.points[(nx, ny)])
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)