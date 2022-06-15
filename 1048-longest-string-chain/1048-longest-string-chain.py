class Solution:    
    def getdist(self, word, hm , words):
        maxd = 1
        for i in range(len(word)):
            sub_word = word[:i] + word[i+1:]
            if sub_word in words:
                if sub_word not in hm:
                    hm[sub_word] = self.getdist(sub_word, hm , words)
                maxd = max(maxd, 1+hm[sub_word])
        return maxd
    
    
    def longestStrChain(self, words: List[str]) -> int:
        maxd, hm = 1, {}
        for word in words:
            if maxd<=len(word):
                hm[word] = self.getdist(word, hm, words)
                maxd = max(maxd, hm[word])
        return maxd

