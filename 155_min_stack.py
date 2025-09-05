class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If there's no element or the value to be pushed is less than 
        # what we have in the min stack, we push the new value to the min stack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        # If not, we still want to just have the smallest value as before
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()