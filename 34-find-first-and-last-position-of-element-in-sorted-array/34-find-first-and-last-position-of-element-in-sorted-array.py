class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs_left(l, r, nums, target):
            idx = -1
            while l <= r:
                mid = l + (r-l)//2
                val = nums[mid]
                
                if val<target:
                    l = mid + 1
                else:
                    r = mid - 1
                if val == target:
                    idx = mid
            return idx
        
        def bs_right(l, r, nums, target):
            idx = -1
            while l <= r:
                mid = l + (r-l)//2
                val = nums[mid]
                
                if val<=target:
                    l = mid + 1
                else:
                    r = mid - 1
                if val == target:
                    idx = mid
            return idx
        
        return [bs_left(0, len(nums)-1, nums, target), bs_right(0, len(nums)-1, nums, target)]