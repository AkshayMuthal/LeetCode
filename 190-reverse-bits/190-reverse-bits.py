class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        cnt = 0
        while n>0:
            ans = ans | (n & 1)
            n >>= 1
            ans <<= 1
            cnt += 1

        ans >>= 1
        for i in range(cnt+1, 33):
            ans <<= 1
        return ans