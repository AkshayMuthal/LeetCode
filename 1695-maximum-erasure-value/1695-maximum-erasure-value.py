class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxs = 0
        csum = 0
        hm = dict()
        l = 0
        for r in range(len(nums)):
            if nums[r] in hm:
                while l<=hm[nums[r]]:
                    csum -= nums[l]
                    l+=1
            csum += nums[r]
            maxs = max(maxs, csum)
            hm[nums[r]] = r
        return maxs