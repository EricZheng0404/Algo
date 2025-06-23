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
        
        time = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):  # fill one round of (n + 1) time units
                if max_heap:
                    task = heapq.heappop(max_heap)
                    if task + 1 != 0:
                        temp.append(task + 1)  # decrease count
                time += 1
                if not max_heap and not temp:
                    break
            for item in temp:
                heapq.heappush(max_heap, item)
        return time

tasks = ["A","A","A","B","B","B"]
n = 2
leastInterval = Solution()
print(leastInterval.leastInterval(tasks, n))