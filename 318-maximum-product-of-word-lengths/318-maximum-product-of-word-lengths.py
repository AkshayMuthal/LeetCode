class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxcnt = 0
        l = len(words)
        mask = [0 for _ in range(l)]
        
        for i, word in enumerate(words):
            for ch in word:
                mask[i] |= (1 << ord(ch)-ord('a'))
            li = len(word)
            
            for j in range(i):
                flag = 0
                if (mask[i] & mask[j] == 0):
                    maxcnt = max(maxcnt, li*len(words[j]))
        return maxcnt