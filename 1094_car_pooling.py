from typing import List
def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = []
        for numPassenger, from, to in trips:class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = []
        for numPassenger, start, end in trips:
            timeline.append((start, numPassenger))
            timeline.append((end, -numPassenger))
        timeline.sort(key=lambda x: (x[0], x[1]))
        curr = 0
        for time, delta in timeline:
            curr += delta
            if curr > capacity:
                return False

        return True