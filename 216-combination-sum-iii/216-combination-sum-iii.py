class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        final_set = []
        self.combisum(1, k, n, [], final_set)
        return final_set

    def combisum(self, ind, k, n, s, final_set):
        if n<0 or k<0:
            return
        if k == 0 and n==0:
            final_set.append(s)
            return
        for i in range(ind, 10):
            self.combisum(i+1, k-1, n-i, s+[i], final_set)