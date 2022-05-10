class Solution:
    def add_param(self, o, c, n, s):
        if o>n or c>n:
            return
        if o+c == 2*n and o==c:
            self.ans.append(s)
        else:
            self.add_param(o+1, c, n, s+"(")
            if c+1<=o:
                self.add_param(o, c+1, n, s+")")
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.add_param(0, 0, n, "")
        return self.ans
