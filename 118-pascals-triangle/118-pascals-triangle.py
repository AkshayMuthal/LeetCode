class Solution:
    def __init__(self):
        self.li = [[1],[1,1]]
        for i in range(2, 31):
            ans = [1]
            prev = self.li[i-1]
            for i in range(len(prev)-1):
                ans.append(prev[i]+prev[i+1])
            ans.append(1)
            self.li.append(ans)
        
    def generate(self, numRows: int) -> List[List[int]]:
        return self.li[0:numRows]
