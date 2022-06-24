class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_range = 0
        for i in range(len(nums)):
            if i>jump_range:
                return False
            jump_range = max(i+nums[i], jump_range)
        return True