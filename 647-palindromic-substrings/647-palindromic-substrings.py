class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        self.count = 0
        
        def get_pallindrome(c, nc): 
            while c>=0 and nc < l and s[c] == s[nc]:
                self.count+=1
                c-=1
                nc+=1  
        
        for i in range(l):
            get_pallindrome(i, i)             
            get_pallindrome(i, i+1)
            
        return self.count
    