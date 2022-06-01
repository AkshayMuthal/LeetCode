class StockSpanner:

    def __init__(self):
        self.stk = deque()
        self.ind = 0

    def next(self, price: int) -> int:
        ans = 1
        # print(self.stk, self.ind, price)
        if len(self.stk) == 0:
            self.stk.append((price, self.ind))
        else:
            while len(self.stk)>0 and price>=self.stk[-1][0]:
                self.stk.pop()
                
            if len(self.stk) == 0:
                ans = self.ind+1
            else:
                ans = self.ind - self.stk[-1][1]
            self.stk.append((price, self.ind))
        self.ind+=1
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)