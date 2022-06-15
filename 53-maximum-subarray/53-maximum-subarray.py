class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = -sys.maxsize 
        s = 0
        for i in nums:
            s+=i
            s = max(s, i)
            maxs = max(maxs, s)
        return maxs