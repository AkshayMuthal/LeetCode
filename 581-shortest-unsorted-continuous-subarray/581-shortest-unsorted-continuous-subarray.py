class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minl = 10001
        flag = 0
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                flag = 1
            if flag:
                minl = min(nums[i], minl)
      
        maxr = -10001
        flag = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>nums[i+1]:
                flag = 1
            if flag:
                maxr = max(nums[i], maxr)
        
        l, r, ns = 0, len(nums)-1, len(nums)
        while l<ns:
            if minl<nums[l]:
                break
            l+=1
        
        while r>=0:
            if maxr>nums[r]:
                break
            r-=1
        if r-l<0:
            return 0
        return r-l+1