from sortedcontainers import SortedDict
class StockPrice:

    def __init__(self):
        # price: Freq hashmap, sorted by price
        self.priceFreq = SortedDict()
        # timestamp: price hashmap
        # we need to know the timestamp's original price
        self.tsPrice = {}
        # Keep track of the latest timestamp
        self.latest = 0

    def update(self, timestamp: int, price: int) -> None:
        # Update the latest ts
        if timestamp > self.latest:
            self.latest = timestamp
        # If we already have this timestamp, we update
        if timestamp in self.tsPrice:
            originalPrice = self.tsPrice[timestamp]
            # We process the originalPrice
            self.priceFreq[originalPrice] -= 1
            if self.priceFreq[originalPrice] == 0:
                del self.priceFreq[originalPrice]
        # Whether we have the ts or not, we need to update self.tsPrice
        self.tsPrice[timestamp] = price
        # We update the new price
        if price in self.priceFreq:
            self.priceFreq[price] += 1
        else:
            self.priceFreq[price] = 1

    def current(self) -> int:
        return self.tsPrice[self.latest]

    def maximum(self) -> int:
        return self.priceFreq.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.priceFreq.peekitem(0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()