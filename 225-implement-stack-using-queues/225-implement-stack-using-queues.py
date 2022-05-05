class MyStack:

    def __init__(self):
        self.stack = deque()
        self.top_elem = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top_elem = x

    def pop(self) -> int:
        temp = deque()
        while len(self.stack)>1:
            v = self.stack.popleft()
            temp.append(v)
            self.top_elem = v
        val = self.stack.popleft()
        self.stack = temp
        return val
        
    def top(self) -> int:
        return self.top_elem

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