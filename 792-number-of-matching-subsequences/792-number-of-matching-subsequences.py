class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        cnt = 0
        dd = defaultdict(list)
        for word in words:
            dd[word[0]].append(word)
        
        for c in s:
            s_matching_strs = dd[c]
            dd[c] = []
            
            for word in s_matching_strs:
                if len(word) == 1:
                    cnt += 1
                else:
                    dd[word[1]].append(word[1:])
        
        return cnt