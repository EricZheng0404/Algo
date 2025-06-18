"""
LeetCode 379. Design Phone Directory
"""

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # Use set to fast check on the membership of the number
        self.available = set()
        for i in range(maxNumbers):
            self.available.add(i)

    def get(self) -> int:
        if self.available:
            return self.available.pop()
        return -1

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        self.available.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)