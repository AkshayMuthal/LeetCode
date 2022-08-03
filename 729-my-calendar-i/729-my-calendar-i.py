class MyCalendar(object):

    def __init__(self):
        self.intervals = []
        # 10 20 30 40 50 60 70 80
        
    def bisect_left(self, start):
        l, r = 0, len(self.intervals)-1
        while l<=r:
            mid = l+(r-l)/2
            if self.intervals[mid][0] == start:
                return mid
            elif self.intervals[mid][0] < start:
                l = mid + 1
            else:
                r = mid - 1
        return l-1
                
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        ind = self.bisect_left(start)
        left, right = False, False
        # print((start, end), self.intervals)
        if ind == -1 or self.intervals[ind][1] <= start:
            left = True
        if ind == len(self.intervals)-1 or end <= self.intervals[ind+1][0]:
            right = True
        # print(left, right)
        if left and right:
            self.intervals.insert(ind+1, (start, end))
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)