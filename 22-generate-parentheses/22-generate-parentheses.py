class Solution:
    def add_param(self, o, c, s):
        if o>self.n or c>self.n:
            return
        if o+c == 2*self.n and o==c:
            self.ans.append(s)
        else:
            self.add_param(o+1, c, s+"(")
            if c+1<=o:
                self.add_param(o, c+1, s+")")
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.n = n
        self.add_param(0, 0, "")
        return self.ans
