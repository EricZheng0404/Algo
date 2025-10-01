class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        schedule = []
        schedule.append((newInterval[0], 1))
        schedule.append((newInterval[1], -1))
        for start, end in intervals:
            schedule.append((start, 1))
            schedule.append((end, -1))
        schedule.sort(key=lambda x:(x[0], -x[1]))
        count = 0
        res = []
        start, end = None, None
        for ts, delta in schedule:
            count += delta
            if count == 1 and start is None:
                start = ts
            if count == 0 and start is not None:
                end = ts
                res.append([start, end])
                start, end = None, None
        return res
        