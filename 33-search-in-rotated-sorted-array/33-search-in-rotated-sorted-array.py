class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l<=h:
            m = l + (h-l)//2
            low, mid, high = nums[l], nums[m], nums[h]
            if mid == target:
                return m
            elif mid >= low: # left side sorted
                if low <= target <= mid:
                    h = m-1
                else:
                    l = m+1
            else:
                if mid <= target <= high:
                    l = m+1
                else:
                    h = m-1
        return -1   
   