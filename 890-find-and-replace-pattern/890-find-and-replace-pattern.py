class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            hm_word = {}
            hm_pat = {}
            check = True
            
            for i in range(len(pattern)):
                if pattern[i] not in hm_pat and word[i] not in hm_word:
                    hm_pat[pattern[i]] = word[i]
                    hm_word[word[i]] = pattern[i]
                elif pattern[i] in hm_pat and word[i] in hm_word:
                    if (hm_pat[pattern[i]] != word[i] or hm_word[word[i]] != pattern[i]):
                        check = False
                        break
                else:
                    check = False
                    break
            if check:
                ans.append(word)
                    
        return ans