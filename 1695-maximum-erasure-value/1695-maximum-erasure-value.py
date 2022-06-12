class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxs = 0
        csum = 0
        hm = dict()
        l = 0
        for r in range(len(nums)):
            val = hm.get(nums[r], -1)
            if val!=-1:
                while l<=val:
                    csum -= nums[l]
                    l+=1
            csum += nums[r]
            maxs = max(maxs, csum)
            hm[nums[r]] = r
        return maxs