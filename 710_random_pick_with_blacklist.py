"""
LeetCode 710. Random Pick with Blacklist

NOTE: Please read all the problem constraints.
In this questions, all elements in blacklist are unique.

"""

"""
The idea is to mvoe all the elments in the blacklist to the back using a mapping.

The possible number we can pick is n - len(blacklist)

Two tricks:
1. If the number to be swapped in the front and the last element to be swapped are both
in the blacklist, then the swapping doesn't have effect.
2. If the to-be-swapped element is already in the back, there's no need to move it.
"""
from typing import List
import random

class Solution:
    
    def __init__(self, n: int, blacklist: List[int]):
        self.size = n - len(blacklist) # we can pick [0, self.size)
        last = n - 1
        self.mapping = {}
        
        for b in blacklist:
            if b >= self.size:
                continue 
            while last in blacklist:
                last -= 1
            self.mapping[b] = last
            last -= 1

    def pick(self) -> int:
        index = random.randint(0, self.size - 1)
        if index in self.mapping:
            return self.mapping[index]
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()