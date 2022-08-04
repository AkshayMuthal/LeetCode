class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stk = []
        ans = [0]*len(temperatures)
        for i, cur_temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < cur_temp:
                ind = stk.pop()
                ans[ind] = i - ind
            stk.append(i)
        return ans