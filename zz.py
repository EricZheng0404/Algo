from collections import deque
from typing import List

def queueSeat(n: List[int]) -> List[int]:
    maxSeat = max(n) + len(n)
    # To track of the seat status
    seat = [False] * (maxSeat)

    # Initialize a seat queue
    q = deque()
    for i in range(len(n)):
        # The queue is a tuple of (index, seat number)
        q.append((i, n[i]))
    
    # The final result to return
    res = [0] * len(n)
    while q:
        # Get the first person in the queue
        index, seatWanted = q.popleft()
        # If the seat is not taken, we can seat the person
        if not seat[seatWanted]:
            seat[seatWanted] = True
            res[index] = seatWanted
        # If the seat is taken, we pushed it back to the end of the queue
        else:
            q.append((index, seatWanted + 1))
    return res

print(queueSeat([1, 2, 3, 2, 4]))