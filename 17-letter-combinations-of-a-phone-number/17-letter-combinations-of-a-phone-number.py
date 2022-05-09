class Solution:
    def combi(self, s, digits, i, n):
        if i==n:
            self.ans.append(s)
            return
        for c in self.map[int(digits[i])]:
            s+=c
            self.combi(s, digits, i+1, n)
            s=s[:-1]
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
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
        self.combi(s, digits, 0, len(digits))
        return self.ans