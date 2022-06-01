class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = deque()
        res = 0
        n = len(heights)
       
        for i in range(len(heights)):
            while stk and heights[stk[-1]]>=heights[i]:
                ind = stk.pop()
                val = heights[ind]*((i - stk[-1] - 1) if stk else i)
                res = max(res, val)
            stk.append(i)
        
        while stk:
            ind = stk.pop()
            val = heights[ind]*((n-stk[-1]-1) if stk else n)
            res = max(res, val)

        return res