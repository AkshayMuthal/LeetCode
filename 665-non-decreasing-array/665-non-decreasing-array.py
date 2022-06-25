class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        replace = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if replace==1:
                    return False
                replace = 1
                if i-2< 0 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True