class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = [0]*k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.maxl = k

    def insertFront(self, value: int) -> bool:
        
        if not self.isFull():
            if self.size == 0:
                self.dq[0] = value
                self.front, self.rear = 0, 0
            else:
                self.front = (self.front - 1)%self.maxl
                self.dq[self.front] = value
            self.size += 1
            # print("insertFront: ", self.dq)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.size == 0:
                self.dq[0] = value
                self.front, self.rear = 0, 0
            else:
                self.rear = (self.front+self.size - 1)%self.maxl
                self.rear = (self.rear+1)%self.maxl
                self.dq[self.rear] = value
            self.size += 1
            # print("insertLast: ", self.dq)
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front+1)%self.maxl
            self.size -= 1
            # print("deleteFront: ", self.dq)
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.rear = (self.front+self.size - 1)%self.maxl
            self.rear = (self.rear - 1)%self.maxl
            self.size -= 1
            # print("deleteLast: ", self.dq)
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        # print("getFront: ", self.dq)
        return self.dq[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # print("getRear: ", self.dq)
        ind = (self.front+self.size-1)%self.maxl
        return self.dq[ind]

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.maxl else False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# 3
# 3 1 2