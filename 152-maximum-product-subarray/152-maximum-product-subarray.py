class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        
        imax = [nums[0]]*l
        imin = [nums[0]]*l
        
        for i in range(1, l):
            mx = imax[i-1]
            mn = imin[i-1]
            if nums[i]<0:
                temp = mx
                mx = mn
                mn = temp
            imax[i] = max(nums[i], nums[i]*mx)
            imin[i] = min(nums[i], nums[i]*mn)
        return max(imax)
                