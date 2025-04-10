import random 

class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        
    def __repr__(self):
        return f"Node(key={self.key}, value={self.value})"

class ArrayHashTable:
    def __init__(self) -> None:
        self.map = {}
        self.arr = []
    
    def put(self, key, value):
        # modify
        if self.containsKey(key):
            i = self.map[key]
            self.arr[i].value = value # I should check full code coverage
            return 
        # add new node
        node = Node(key, value)
        self.arr.append(node)
        self.map[key] = len(self.arr) - 1

    def remove(self, key):
        if key not in self.map:
            return 
        index = self.map[key] # the index in the arr
        curr_node = self.arr[index] # the node(key, value) we have
        last_node = self.arr[-1] # the last node now in the arr

        self.arr[index] = last_node 
        self.arr[-1] = curr_node 
        self.arr.pop()

        self.map[last_node.key] = index
        self.map.pop(key)
    
    def containsKey(self, key):
        return key in self.map
    
    def randomKey(self):
        if len(self.arr) == 0:
            return None
        index = random.randint(0, len(self.arr) - 1)
        return self.arr[index].key
    
def test_put():
    my = ArrayHashTable()
    my.put(1, 2)
    assert my.containsKey(1)
    assert my.arr[0].value == 2
    assert my.map[1] == 0

def test_remove():
    my = ArrayHashTable()
    my.put(1, 1)
    my.put(2, 2)
    my.put(3, 3)
    my.remove(1)
    print(my.map)
    print(my.arr)

def test_randomKey():
    my = ArrayHashTable()
    my.put(1, 1)
    my.put(2, 2)
    my.put(3, 3)
    print(my.randomKey())
    

# test_put()
# test_remove()
# test_randomKey()
