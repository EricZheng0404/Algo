from collections import defaultdict
class TimeMap:
    """
    The key is that the timestamps are numbers, and they're sorted in the list: "
    All the timestamps are strictly increasing." So, we can use this number as the 
    searching target using binary search.
    """
    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.lookup:
            self.lookup[key] = []
        self.lookup[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.lookup[key]
        index = self.rightBound(lst, timestamp)
        # I forgot this. If index is -1, that means there's no timestamp_prev.
        if index == -1:
            return ""
        return lst[index][0]

    def rightBound(self, lst, target):
        l, r = 0, len(lst)
        while l < r:
            mid = l + (r - l) // 2
            if lst[mid][1] <= target:
                l = mid + 1
            else:
                r = mid 
        if l - 1 < 0:
            return -1
        return l - 1

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)