class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        
        imax, imin, amax = nums[0], nums[0], nums[0]
        
        for i in range(1, l):
            if nums[i]<0:
                temp = imax
                imax = imin
                imin = temp
            imax = max(nums[i], nums[i]*imax)
            imin = min(nums[i], nums[i]*imin)
            amax = max(imax, amax)
        return amax