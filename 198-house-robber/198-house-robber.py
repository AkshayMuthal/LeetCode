class Solution:
    def rob(self, nums: List[int]) -> int:
        dp, dp1, dp2 = 0, 0, 0
        
        for i in range(len(nums)):
            dp = max(dp1, dp2+nums[i])
            dp2 = dp1
            dp1 = dp
        
        return dp