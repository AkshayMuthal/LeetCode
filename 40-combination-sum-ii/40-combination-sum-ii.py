class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.dfs(target, [], [], sorted(candidates), 0)
    
    def dfs(self, target, path, res, candidates, old):
        if target < 0:
            return res
        if target == 0:
            res.append(path)
            return res
        for i in range(old, len(candidates)):
            if i>old and candidates[i]==candidates[i-1]:
                continue    
            res = self.dfs(target - candidates[i], path + [candidates[i]], res, candidates, i+1)
        return res
    