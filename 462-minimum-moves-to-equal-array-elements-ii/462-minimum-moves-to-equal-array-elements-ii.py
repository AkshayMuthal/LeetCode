class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves, l, r = 0, 0, len(nums)-1
        while l<=r:
            moves += nums[r]-nums[l]
            r-=1
            l+=1
        return moves