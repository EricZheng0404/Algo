class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        After sorting the intervals, we don't really about the starts of the intervals.
        Because the start of the previous interval will be either smaller or the same as
        the later one.

        
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for interval in intervals:
            # Case 3: there's no overlap            
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # Case 1: The latter interval is fully covered by the previous
            # Case 2: There is an overlap
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res