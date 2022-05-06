class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)-1
        
        while digits[l]==9:
            digits[l] = 0
            l-=1
        if l<0:
            digits = [1] + digits
        else:
            digits[l]+=1
        
        return digits