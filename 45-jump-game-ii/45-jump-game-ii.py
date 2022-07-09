class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach = 0
        min_steps = sys.maxint
        l = len(nums)
        dp = [0]*l
        for i in range(l-2, -1, -1):
            curr_min = sys.maxint
            for j in range(i+1, i+1+nums[i]):
                if j>=l:
                    break
                curr_min = min(curr_min, 1+dp[j])
            dp[i] = curr_min
        return dp[0]
