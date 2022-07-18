class Solution(object):
    def dfs(self, target, path, res, candidates):
        if target < 0:
            return res
        if target == 0:
            res.append(path)
            return res
        for i in range(len(candidates)):
            res = self.dfs(target - candidates[i], path + [candidates[i]], res, candidates[i:])
        return res
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.dfs(target, [], [], candidates)