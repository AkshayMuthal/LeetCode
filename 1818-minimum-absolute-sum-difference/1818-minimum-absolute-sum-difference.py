import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9+7
        abs_a = 0
        abs_diff = []
        n = len(nums1)
        
        for i in range(n):
            diff = abs(nums1[i]-nums2[i])
            abs_diff.append(diff)
            abs_a+=diff
        
        nums1.sort()
        mine = abs_a
        
        for i in range(n):
            diff = abs_diff[i]
            ind = bisect.bisect_left(nums1, nums2[i])
            
            if ind<n:
                mine = min(mine, abs_a - diff + abs(nums2[i]-nums1[ind]))
            if ind>0:
                mine = min(mine, abs_a - diff + abs(nums2[i]-nums1[ind-1]))
        
        return mine % mod
