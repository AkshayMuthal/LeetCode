class Solution:
    def get_count(self, nums, amount, l, dp):
        if amount == 0:
            return 1
        if dp[amount]!=-1:
            return dp[amount]
        
        count = 0
        for i in range(l):
            if nums[i]<=amount:
                count += self.get_count(nums, amount-nums[i], l, dp)
        
        dp[amount] = count
        return count
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1 for _ in range(target+1)]
        return self.get_count(nums, target, len(nums), dp)
        