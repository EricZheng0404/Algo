class HitCounter:

    def __init__(self):
        self.index = deque()

    def hit(self, timestamp: int) -> None:
        self.index.append(timestamp)
        if self.index and self.index[0] <= timestamp - 300:
            self.index.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.index and self.index[0] <= timestamp - 300:
            self.index.popleft()
        return len(self.index)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)