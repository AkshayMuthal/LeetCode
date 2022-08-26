class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def traverse(ind, curr, nums, super_set):
            if ind >= len(nums):
                return
            super_set.append(curr)
            for i in range(ind+1, len(nums)):
                traverse(i, curr+[nums[i]], nums, super_set)
        
        super_set = [[]]
        for i in range(len(nums)):
            traverse(i, [nums[i]], nums, super_set)
        
        return super_set
            