class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        asum = 0
        
        for i in nums:
            asum+=i
        if asum == x:
            return len(nums)
        elif asum<x:
            return -1
        
        target = asum-x
        al = len(nums)
        l, r, csum, maxlen = 0, 0, 0, -1
        
        while r<al:
            if csum <= target:
                if csum == target:
                    maxlen = max(maxlen, r-l)
                csum += nums[r]
                r += 1
            while csum>target and l<=r:
                csum -= nums[l]
                l += 1
            
        if csum == target:
            maxlen = max(maxlen, r-l)
        
        return al-maxlen if maxlen>=0 else -1