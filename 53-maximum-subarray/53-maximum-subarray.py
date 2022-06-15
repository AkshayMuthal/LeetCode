class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = -sys.maxsize 
        s = 0
        for i in nums:
            s+=i
            maxs = max(maxs, s)
            if s <0:
                s=0
        return maxs