class Solution:
    def combi(self, s, i):
        if i==self.len:
            self.ans.append(s)
            return
        for c in self.map[int(self.digits[i])]:
            s += c
            self.combi(s,i+1)
            s = s[:-1]
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        self.digits = digits
        self.len = len(digits)
        self.map = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        s = ""
        self.ans = []
        self.combi(s, 0)
        return self.ans