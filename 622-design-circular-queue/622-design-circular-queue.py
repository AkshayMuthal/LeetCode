class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0]*k
        self.front = -1
        self.rear = -1
        self.size = 0
        self.l = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.front+self.size-1)%self.l
            self.rear = (self.rear+1)%self.l
            self.q[self.rear] = value
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front+1)%self.l
            self.size -= 1
            if self.isEmpty():
                self.front = 0
                self.rear = 0
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.q[self.front]
        return -1
        
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.q[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size>=self.l else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()