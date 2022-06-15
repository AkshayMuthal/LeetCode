class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        ans = [1 for _ in range(l)]
        for i in range(1, l):
            ans[i] = ans[i-1]*nums[i-1]

        pro = nums[l-1]
        for i in range(l-2, -1, -1):
            ans[i] = pro*ans[i]
            pro *= nums[i]
        
        return ans