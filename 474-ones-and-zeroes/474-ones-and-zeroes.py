class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mp = {}
        l = len(strs)
        for i in range(len(strs)):
            o = 0
            z = 0
            for c in strs[i]:
                if c == '1':
                    o+=1
                else:
                    z+=1
            mp[i] = [z, o]
        
        dp=[[[-1 for col in range(n+1)] for col in range(m+1)] for row in range(l)]
        
        def traverse(ind, nzeros, nones):
            if ind == l or (nzeros == 0 and nones == 0):
                return 0
            if dp[ind][nzeros][nones]!=-1:
                return dp[ind][nzeros][nones]
            
            zero = mp[ind][0]
            one = mp[ind][1]
            if zero>nzeros or one>nones:
                dp[ind][nzeros][nones] = traverse(ind+1, nzeros, nones)
                return dp[ind][nzeros][nones]
            
            ans_with_index = 1 + traverse(ind+1, nzeros-zero, nones-one)
            ans_without_index = traverse(ind+1, nzeros, nones)
            
            dp[ind][nzeros][nones] = max(ans_with_index, ans_without_index)
            return dp[ind][nzeros][nones]
        
        dp[0][m][n] = traverse(0, m, n)
        return dp[0][m][n]
        
    def findMaxFormold(self, strs: List[str], m: int, n: int) -> int:
        mp = []
        l = len(strs)
        for s in strs:
            o = 0
            z = 0
            for c in s:
                if c == '1':
                    o+=1
                else:
                    z+=1
            mp.append([z, o])
        
        res = []
        
        def traverse(i, z, o, sl):
            if i>=l:
                return
            
            z += mp[i][0]
            o += mp[i][1]
            if z>m or o>n:
                return
            
            res.append(sl)
            # print(res)
            for ind in range(i+1, l):
                traverse(ind, z, o, sl+1)
        
        for i in range(l):
            traverse(i, 0, 0, 1)
        
        maxr = 0
        for i in res:
            maxr = max(i, maxr)
        
        return maxr
                