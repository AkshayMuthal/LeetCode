class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        s = len(self.stack)
        while s>1:
            self.stack.append(self.stack.popleft())
            s-=1

    def pop(self) -> int:
        return self.stack.popleft()
        
    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()