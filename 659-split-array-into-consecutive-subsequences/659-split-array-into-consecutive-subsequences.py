class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        right = collections.Counter()
        
        for num in nums:
            if left[num] == 0: 
                continue
            left[num] -= 1
            if right[num-1]>0:
                right[num-1] -= 1
                right[num] += 1
            elif left[num+1]>0 and left[num+2]>0:
                left[num+1] -= 1
                left[num+2] -= 1
                right[num+2] += 1
            else:
                return False
        return True
            