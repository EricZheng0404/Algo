class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        # Look at the constraints. All the given intervals are unique, so there's no 
        # need to record all the intervals. And l and r starts from 0
        prev = 0
        count = 0
        for start, end in intervals:
            if end > prev:
                count += 1
                prev = end
        return count