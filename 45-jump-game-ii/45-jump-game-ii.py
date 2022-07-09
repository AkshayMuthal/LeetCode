class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps, reach, end = 0, 0, 0
        l = len(nums)
        for i in range(l-1):
            reach = max(reach, i + nums[i])
            if i == end:
                steps += 1
                end = reach
        return steps
