class Logger:

    def __init__(self):
        self.prev = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.prev:
            if timestamp - self.prev[message] >= 10:
                self.prev[message] = timestamp
                return True
            else:
                return False
        else:
            self.prev[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)