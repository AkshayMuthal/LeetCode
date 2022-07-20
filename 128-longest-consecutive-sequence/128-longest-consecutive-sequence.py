class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        ms = 0
        for num in nums:
            if num+1 not in nums:
                cs = 1
                while num-1 in nums:
                    cs += 1
                    num -= 1
                ms = max(ms, cs)
        return ms
    