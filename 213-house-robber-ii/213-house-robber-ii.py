class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for i in range(l)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, l-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        v1 = dp[l-2]
        
        dp[0] = 0
        dp[1] = nums[1]
        
        for i in range(2, l):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return max(v1, dp[l-1])
        