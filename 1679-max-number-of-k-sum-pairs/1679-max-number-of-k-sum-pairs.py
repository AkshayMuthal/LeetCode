class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        cnt = 0
        for i in nums:
            if k-i in hm and hm[k-i]>0:
                cnt+=1
                hm[k-i]-=1
            else:
                hm[i]+=1
        return cnt