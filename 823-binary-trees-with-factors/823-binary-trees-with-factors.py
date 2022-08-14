class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        N = len(arr)
        arr.sort()
        dp = [1]*N
        index = {val:ind for ind, val in enumerate(arr)}
        
        for i in range(N):
            for j in range(i):
                if arr[i]%arr[j] == 0:
                    right = arr[i]/arr[j]
                    if right in index:
                        dp[i] += dp[j]*dp[index[right]]
                        dp[i] %= MOD
        
        return sum(dp)%MOD