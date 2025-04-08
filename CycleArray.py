# Left-closed, right-open CycleArray
class CycleArray:
    def __init__(self, size = 1):
        self.size = size # Size of the array
        self.arr = [None] * size # Create an array of size
        self.start = 0 # The first element
        self.end = 0 # The index of the position after the last valid element
        self.count = 0 # The number of the elements
        
    def resize(self, newSize):
        newArr = [None] * newSize
        for i in range(self.count):
            newArr[i] = self.arr[(self.start + i) % self.size]
        self.arr = newArr
        self.size = newSize
        self.start = 0
        self.end = self.count
    
    
    def add_first(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        self.start = (self.start - 1 + self.size) % self.size
        self.arr[self.start] = val
        self.count += 1
    
    def remove_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
    
    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        self.arr[self.end] = val 
        self.end = (self.end + 1) % self.size
        self.count += 1
    
    def remove_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        self.end = (self.end - 1 + self.size) % self.size
        self.arr[self.end] = None
        self.count -= 1

    def get_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[self.start]
    
    def get_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[(self.end - 1 + self.size) % self.size]
    
    def is_full(self):
        return self.count == self.size
    
    # return the number of elements in the CycleArray
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.count == 0
    
    def all_elements(self):
        if self.is_empty():
            raise Exception("Array is empty")
        result = ""
        for i in range(self.count):
            result += str(self.arr[(self.start + i) % self.size])
        return result
            


def test_resize():
    cycle = CycleArray(5)
    assert cycle.size == 5
    assert cycle.arr == [None] * 5
    cycle.resize(10)
    assert cycle.size == 10
    
def test_add_first():
    cycle = CycleArray(5)
    cycle.add_first(1)
    assert cycle.arr == [None, None, None, None, 1]
    cycle.add_first(2)
    assert cycle.arr == [None, None, None, 2, 1]
    assert cycle.count == 2
    
def test_remove_first():
    cycle = CycleArray(5)
    # cycle.remove_first()
    cycle.add_first(1)
    cycle.add_first(2)
    cycle.add_first(3)
    cycle.add_first(4)
    cycle.add_first(5)
    print(cycle.arr)
    cycle.remove_first()
    print(cycle.arr)


def test_add_last():
    cycle = CycleArray(5)
    cycle.add_last(1)
    cycle.add_last(2)
    cycle.add_last(3)
    cycle.add_last(4)
    cycle.add_last(5)
    cycle.add_last(1)
    cycle.add_first(1)
    cycle.remove_first()
    assert cycle.count == 6
    assert cycle.start == 0
    assert cycle.end == 6

def test_remove_last():
    cycle = CycleArray()
    cycle.add_last(1)
    cycle.add_last(2)
    cycle.add_last(3)
    cycle.add_last(4)
    cycle.add_last(5)
    cycle.add_last(1)
    cycle.remove_last()
    assert cycle.count == 5
    assert cycle.start == 0
    assert cycle.end == 5

def test_get_first():
    cycle = CycleArray()
    cycle.add_last(1)
    cycle.add_last(2)
    cycle.add_last(3)
    cycle.add_last(4)
    cycle.add_last(5)
    cycle.add_first(1)
    assert cycle.get_first() == 1
    assert cycle.count == 6
    print(cycle.arr)
    print(cycle.all_elements())


# test_resize()
# test_add_first()
# test_remove_first()
test_add_last()
test_remove_last()
test_get_first()
print("All tests passed!")
