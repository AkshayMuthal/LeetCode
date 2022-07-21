class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        
        hm = defaultdict()
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], []) + [i]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = -(nums[i]+nums[j])
                if target in hm:
                    if target == nums[i] and len(hm[target])<2:
                        continue
                    if target == nums[j] and len(hm[target])<2:
                        continue
                    if target == nums[i] == nums[j] and len(hm[target])<3:
                        continue
                    ans.add(tuple(sorted([nums[i], nums[j], target])))
        
        return ans