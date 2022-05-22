class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        sl = len(s)
        pl = len(p)
        
        if pl>sl:
            return ans
        
        char = 256
        cp = [0]*char
        cs = [0]*char
        
        for i in range(pl):
            cp[ord(p[i])]+=1
        # if cs == cp:
        #     ans.append(0)
        
        for i in range(sl):
            cs[ord(s[i])]+=1
            if i>=pl:
                cs[ord(s[i-pl])]-=1
            if cs == cp:
                ans.append(i-pl+1)
        return ans
