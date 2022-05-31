class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        window = 0
        all_one = need-1
        got = [False]*need
            
        for i in range(len(s)):
            window = ((window<<1) & all_one) | int(s[i])
            
            if i >= k-1 and got[window] is False:
                got[window] = True
                need-=1
                if need == 0:
                    return True
        return False
