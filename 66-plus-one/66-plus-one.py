class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = l - 1
        
        old = digits[i]
        digits[i] = int((old+1)%10)
        c = int((old+1)/10)
        i-=1

        while i>=0:
            old = digits[i]
            digits[i] = int((old+c)%10)
            c = int((old+c)/10)
            i-=1
        
        if c >=1:
            newL = [c]
            for i in digits:
                newL.append(i)
            return newL
        else:
            return digits