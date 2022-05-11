class Solution:
    def cnt(self, ind, l):
        if l > self.n:
            return
        if l == self.n:
            self.ans+=1
            return
        for i in range(ind, 5):
            self.cnt(i, l+1)
    
    def countVowelStrings(self, n: int) -> int:
        self.n = n
        self.ans = 0
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.cnt(0, 0)
        return self.ans