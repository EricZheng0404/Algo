"""
LeetCode 1429. First Unique Number

You have a queue of integers, you need to retrieve the first unique integer in the
queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
"""
from typing import List
from collections import Counter

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.count = {}
        for num in nums:
            self.add(num)

    # O(1) time complexity for showFirstUnique because each number is added
    # once and popped once.
    def showFirstUnique(self) -> int:
        while self.q:
            # If the first number is not unique, continuously pop it until we
            # find a unique number.
            if self.count[self.q[0]] > 1:
                self.q.pop(0)
            else:
                return self.q[0]
        return -1

    def add(self, value: int) -> None:
        if value in self.count:
            self.count[value] += 1
        else:
            self.count[value] = 1
        self.q.append(value)

firstUnique = FirstUnique([2, 3, 5])
print(firstUnique.showFirstUnique())
firstUnique.add(5)
print(firstUnique.showFirstUnique())
firstUnique.add(2)
print(firstUnique.showFirstUnique())
firstUnique.add(3)
print(firstUnique.showFirstUnique())