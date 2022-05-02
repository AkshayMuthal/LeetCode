class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e, o = 0, len(nums)-1
        while e<o:
            while e<len(nums) and nums[e]%2==0:
                e+=1
            while o>=0 and nums[o]%2!=0:
                o-=1
            if e<o:
                temp = nums[e]
                nums[e] = nums[o]
                nums[o] = temp
                e+=1
                o-=1
            else:
                break
        return nums