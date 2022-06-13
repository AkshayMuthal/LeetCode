class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(4):
            v = i
            cnt = 0
            while v>0:
                if v&1:
                    cnt+=1
                v>>=1
            ans.append(cnt)
        
        if 0<=n<=3:
            return ans[:n+1]
        
        x = len(ans)
        while x<=n:
            for i in range(len(ans)):
                if x+i>n:
                    break
                ans.append(ans[i]+1)
            x = len(ans)
            
        return ans