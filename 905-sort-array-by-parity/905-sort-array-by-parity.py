class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l = len(nums)
        e, o = 0, l-1
        
        while e<o:
            if nums[e]%2==0:
                e+=1
            elif nums[o]%2!=0:
                o-=1
            else:
                temp = nums[e]
                nums[e] = nums[o]
                nums[o] = temp
                o-=1
                e+=1
        return nums
                