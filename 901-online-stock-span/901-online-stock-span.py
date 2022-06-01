class StockSpanner:

    def __init__(self):
        self.stk = deque()
        self.ind = 0

    def next(self, price: int) -> int:
        ans = 0
        while self.stk and price>=self.stk[-1][0]:
            self.stk.pop()

        ans = self.ind - (self.stk[-1][1] if self.stk else -1)
        self.stk.append((price, self.ind))
        
        self.ind+=1
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)