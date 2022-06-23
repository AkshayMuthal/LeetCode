class Solution:
    def binary_search(self, lis, target):
        l, r = 0, len(lis)-1
        ans = -1
        while l<=r:
            mid = int(l + (r-l)/2)
            if lis[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        l = len(nums)
        for i in range(1, l):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                ind = self.binary_search(lis, nums[i])
                lis[ind] = nums[i]
        return len(lis)