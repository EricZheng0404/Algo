from collections import deque
from typing import List

"""
LeetCode 

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely
and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each
move consists of turning one wheel one slot.

"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends:
            return -1
        
        start = "0000"
        visited = set()
        visited.add(start)
        q = deque()
        q.append(start)
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                curr = q.popleft()
                if curr == target:
                    # If the start (0000) is the target, we should directly return 0
                    return step
                for change in self.possibleChange(curr):
                    if change not in deadends and change not in visited:
                        visited.add(change)
                        q.append(change)

            step += 1
        return -1
    
    def possibleChange(self, curr):
        res = []
        for i in range(len(curr)):
            res.append(self.plus(curr, i))
            res.append(self.minus(curr, i))
        return res

    def plus(self, wheels, index):
        res = list(wheels)
        if res[index] == '9':
            res[index] = '0'
        else:
            res[index] = str(ord(res[index]) - ord('0') + 1)
        return "".join(res)
    
    def minus(self, wheels, index):
        res = list(wheels)
        if res[index] == '0':
            print("hello")
            res[index] = '9'
        else:
            res[index] = str(ord(res[index]) - ord('0') - 1)
        return "".join(res)
    
sol = Solution()
print(sol.openLock(["0201","0101","0102","1212","2002"], "0009"))