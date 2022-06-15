class Solution:    
    def getdist(self, word, d, hm , words):
        maxd = d
        for i in range(len(word)):
            sub_word = word[:i] + word[i+1:]
            if sub_word in words:
                if sub_word not in hm:
                    hm[sub_word] = self.getdist(sub_word, 1, hm , words)
                maxd = max(maxd, d+hm[sub_word])
        return maxd
    
    
    def longestStrChain(self, words: List[str]) -> int:
        maxd, hm = 1, {}
        for word in words:
            hm[word] = self.getdist(word, 1, hm, words)
        for k, v in hm.items():
            maxd = max(maxd, v)
        return maxd