class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxcnt = 0
        l = len(words)
        
        for i in range(l):
            ca = [0 for _ in range(256)]
            for c in words[i]:
                ca[ord(c)]+=1
            li = len(words[i])
            
            for j in range(i+1, l):
                flag = 0
                for w in words[j]:
                    if ca[ord(w)]>0:
                        flag = 1
                        break
                if flag == 0:
                    maxcnt = max(maxcnt, li*len(words[j]))
        return maxcnt