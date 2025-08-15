from typing import List, Optional
"""
292. Nim Game

If I want to win in the last round, I need to a have a number of 1 to 3
stones. That leaves my opponent with a number of 4 stones.
This means in the round before that, I need to have a number of 5 to 7
stones. That leaves my opponent with a number of 8 stones.
As long as the number of stones is not divisible by 4, I can win.
"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n % 4 == 0