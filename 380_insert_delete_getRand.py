"""
LeetCode 380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

class RandomizedSet:

    def __init__(self):
        self.array = [] # [val1, val2, val3...]
        self.index = {} # val: index

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        index = len(self.array)
        self.array.append(val)
        self.index[val] = index
        return True

    def remove(self, val: int) -> bool:
        # Return False when the item is not present
        if val not in self.index:
            return False
        # If present, we need to swap its position with the last element 
        currIndex = self.index[val]
        lastElement = self.array[-1]
        # lastElementIndex = self.index[lastElement]
        self.array[currIndex] = lastElement
        # self.array[lastElementIndex] = val # But we don't need to put the val back to the last element
        self.array.pop() # I forgot to pop the last element, or the last element will be at two places
        # self.index[val] = lastElementIndex
        self.index[lastElement] = currIndex
        del self.index[val] # I forgot to remove the element fromt the dictionoary
        return True # I forgot to return True at last


    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()