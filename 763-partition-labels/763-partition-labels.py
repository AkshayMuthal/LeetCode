class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hm = {}
        for i, c in enumerate(s):
            hm[c] = i
        
        start, latest_last_ind = 0, 0
        ans = []
        for i, c in enumerate(s):
            latest_last_ind = max(latest_last_ind, hm[c])
            if i == latest_last_ind:
                ans.append(latest_last_ind - start + 1)
                start = i+1
        return ans