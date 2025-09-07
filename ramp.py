"""
Your task is to implement a Rate Limiter. Given a list of timestamped 
queries, you will need to accept of decline each of them.

The queries are represented by two arrays, `timestamps` and `ipAddresses`.
- timestamps: a list of timestamps
- ipAddresses: a list of IP addresses

You are also given two integers `limit` and `timeWindow`:
- limit: represents the maximum number of requests that can be made in the time 
window.
- timeWindow: represents the duration of the inclusive time window.
"""
from collections import defaultdict, deque
def RateLimiter(timestamps, ipAddresses, limit, timeWindow):
    res = []
    index = defaultdict(deque)
    for t, ip in zip(timestamps, ipAddresses):
        curr = index[ip]
        if curr and curr[0] < t - timeWindow:
            curr.popleft()
        # If we have less than the limit, we can add the request
        if len(curr) < limit:
            index[ip].append(t)
            res.append(1)
        # If we have more than the limit, we can't add the request
        else:
            res.append(0)
        
    return res


test1 = [
    [954, 957, 958], # timestamps
    ["211", "211", "211"], # ipAddresses
    1, # limit
    3, # timeWindow
]

test2 = [
    [0, 0, 0],
    [49, 38, 38],
    2, 
    10
]
print(RateLimiter(*test1))
print(RateLimiter(*test2))
assert RateLimiter(*test1) == [1, 0, 1]
assert RateLimiter(*test2) == [1, 1, 1]