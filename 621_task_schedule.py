"""
621. Task Scheduler
"""

from typing import List

from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]  # max heap, so use negative values
        heapq.heapify(max_heap)
        print(max_heap)

tasks = ["A","A","A","B","B","B"]
n = 2
leastInterval = Solution()
print(leastInterval.leastInterval(tasks, n))