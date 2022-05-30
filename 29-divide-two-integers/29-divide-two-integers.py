class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        ans = 0
        divs = True if (dividend<0) else False
        ds = True if (divisor<0) else False
        sign = True if (divs == ds) else False
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend-divisor >= 0:
            q = 0 
            while dividend > (divisor << (q+1)):
                q+=1
            ans += 1<<q
            dividend -= divisor<<q
        if ans == 1<<31 and sign:
            return 2147483647
        return ans if sign else -ans