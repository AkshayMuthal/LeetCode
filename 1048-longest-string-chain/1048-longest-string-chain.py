class Solution:    
    def getdist(self, word, hm , words):
        maxd = 1
        for i in range(len(word)):
            sub_word = word[:i] + word[i+1:]
            maxd = max(maxd, hm.get(sub_word, 0)+1)
        return maxd
    
    
    def longestStrChain(self, words: List[str]) -> int:
        maxd, hm = 1, {}
        for word in sorted(words, key=len):
            hm[word] = self.getdist(word, hm, words)
            maxd = max(maxd, hm[word])
        return maxd

