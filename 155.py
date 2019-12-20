class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_stack = []

    def push(self, x: int) -> None:
        self.my_stack.append(x)

    def pop(self) -> None:
        self.my_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]


    def getMin(self) -> int:
        return min(self.my_stack)

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
