import collections

"""
Leetcode 146: LRU Cache
This is a design problem.
"""

class LRUCache:
    # Hash-linked list
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.makeLast(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache, we update the value and move it to the end.
        if key in self.cache:
            self.makeLast(key)
            self.cache[key] = value
            
        # If the key is not in the cache, we add it to the cache.
        else:
            if len(self.cache) == self.capacity:
                first_key = next(iter(self.cache))
                del self.cache[first_key]

            self.cache[key] = value
        
    def makeLast(self, key: int) -> None:
        value = self.cache.pop(key)
        self.cache[key] = value

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    print(lru.cache)