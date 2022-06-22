class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n 
        m2, m1 = 1, 2
        for i in range(2, n):
            temp = m1
            m1 = m1 + m2
            m2 = temp
        return m1
            