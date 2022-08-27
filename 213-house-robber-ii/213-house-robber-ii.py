class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 1:
            return nums[0]
        
        dp, dp1, dp2 = 0, 0, 0
        for i in range(l-1):
            dp = max(dp1, dp2+nums[i])
            dp2 = dp1
            dp1 = dp
        
        ans1 = dp
        dp, dp1, dp2 = 0, 0, 0
        for i in range(1, l):
            dp = max(dp1, dp2+nums[i])
            dp2 = dp1
            dp1 = dp
        
        return max(dp, ans1)