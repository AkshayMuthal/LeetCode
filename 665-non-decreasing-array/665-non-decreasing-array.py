class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        replace = False
        l = len(nums)
        
        for i in range(1, l):
            if nums[i-1] > nums[i]:
                if replace:
                    return False
                replace = True
                if i-2< 0 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True