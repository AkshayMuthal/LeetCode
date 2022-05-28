class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sa = int((n*(n+1))/2)
        sc = 0
        for i in nums:
            sc+=i
        return sa-sc