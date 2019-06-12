class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3,param_4)