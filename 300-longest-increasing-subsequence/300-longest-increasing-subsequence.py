class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0,3,1,6,2,2,7
        # 4,3,3,2,1,1,1
        ans = [1]*len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            tm = 0
            for j in range(i+1, len(nums)):
                if nums[j]>nums[i]:
                    tm = max(tm, ans[j])
            ans[i] += tm
        return max(ans)