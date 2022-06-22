class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, mine = 0, len(nums)-1, sys.maxsize
        
        while l<=r:
            mid = int(l + (r-l)/2)
            if nums[mid]>=nums[l]:
                mine = min(mine, nums[l])
                l = mid+1
            else:
                mine = min(mine, nums[mid])
                r = mid-1

        return mine