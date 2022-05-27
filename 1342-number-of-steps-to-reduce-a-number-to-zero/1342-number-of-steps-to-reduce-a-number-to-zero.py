class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        if num == 0:
            return cnt
        while num>0:
            if num & 1 == 1:
                cnt += 1
            num = num >> 1
            cnt+=1
        return cnt-1