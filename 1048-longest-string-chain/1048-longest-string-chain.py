class Solution:    
    def longestStrChain(self, words: List[str]) -> int:
        maxd, hm = 1, {}
        for word in sorted(words, key=len):
            hm[word] = 1
            for i in range(len(word)):
                sub_word = word[:i] + word[i+1:]
                hm[word] = max(hm[word], hm.get(sub_word, 0)+1)
            maxd = max(maxd, hm[word])
        return maxd

