class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num>0:
            if num & 1 == 1:
                #odd
                num = num >> 1
                num = num << 1
            else:
                #even
                num = num >> 1
            cnt+=1
        return cnt