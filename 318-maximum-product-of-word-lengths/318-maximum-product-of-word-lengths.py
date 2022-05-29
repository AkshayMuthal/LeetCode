class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxcnt = 0
        mask = [0 for _ in range(len(words))]
        
        for i, word in enumerate(words):
            for ch in word:
                mask[i] |= (1 << ord(ch)-ord('a'))
            li = len(word)
            
            for j in range(i):
                if (mask[i] & mask[j] == 0):
                    maxcnt = max(maxcnt, li*len(words[j]))
        return maxcnt