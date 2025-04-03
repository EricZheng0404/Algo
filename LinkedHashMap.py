class MyLinkedHashMap:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
            
    def __init__(self):
        self.map = {}
        self.head = self.Node(None, None) # Head and tail are both dummy nodes
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        if key not in self.map:
            return None
        return self.map[key]
    
    def put(self, key, value):
        if key in self.map:
            return 
        else:
            new_node = self.Node(key, value)
            self.map[key] = new_node # We put a node here instead of value
            self.add_last_node(new_node)
    
    def remove(self, key):
        if key not in self.map:
            return 
        else:
            node = self.map[key]
            self.remove_node(node)
            del self.map[key]
    
    def contains_key(self, key):
        return key in self.map
    # true if key is in map, false if not
    
    def keys(self): 
        temp = self.head.next
        result = ""
        while temp != self.tail:
            result += str(temp.key) + ", "
            temp = temp.next
        result = result.rstrip(", ")
        return result
    

    def add_last_node(self, node):
         temp = self.tail.prev
         temp.next = node
         node.prev = temp
         node.next = self.tail
         self.tail.prev = node
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    
    
if __name__ == "__main__":
    map = MyLinkedHashMap()
    map.put(1, "a")
    map.put(2, "b")
    print(map.contains_key(1))
    print(map.contains_key(2))
    print(map.keys())
