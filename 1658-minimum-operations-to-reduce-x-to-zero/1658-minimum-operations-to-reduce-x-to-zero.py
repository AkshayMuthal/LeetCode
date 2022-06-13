class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        asum = 0
        for i in nums:
            asum+=i
        
        target = asum-x
        al = len(nums)
        l, csum, maxlen = 0, 0, -1
        
        for r in range(al):
            csum += nums[r]
            while csum>target and l<=r:
                csum -= nums[l]
                l += 1
            if csum == target:
                maxlen = max(maxlen, r-l+1)
        
        return al-maxlen if maxlen>=0 else -1
