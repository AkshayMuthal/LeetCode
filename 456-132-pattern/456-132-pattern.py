class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = len(nums)-1
        amin = [0 for i in range(l+1)]
        amax = deque()
        amin[0] = nums[0]

        for i in range(1, len(nums)):
            amin[i] = min(amin[i-1], nums[i])
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i]>amin[i]:
                while len(amax)>0 and amax[-1]<=amin[i]:
                    amax.pop()
                if len(amax)>0 and nums[i]>amax[-1]:
                    return True
                amax.append(nums[i])
        return False