class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        prev = [1]
        for i in range(1, numRows):
            curr = [1]
            for j in range(1, len(prev)):
                curr.append(prev[j]+prev[j-1])
            curr.append(1)
            prev = curr
            ans.append(curr)
        return ans