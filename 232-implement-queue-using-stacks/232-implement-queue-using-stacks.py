class MyQueue(object):

    def __init__(self):
        self.stack = deque()
        self.pop_stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
    
    def pop(self):
        """
        :rtype: int
        """
        if len(self.pop_stack) == 0:
            while self.stack:
                self.pop_stack.append(self.stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.pop_stack) == 0:
            while self.stack:
                self.pop_stack.append(self.stack.pop())
        return self.pop_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack)==0 and len(self.pop_stack)==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

