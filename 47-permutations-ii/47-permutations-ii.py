from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permute(comb, counter):
            if len(comb) == len(nums):
                result.append(list(comb))
                return
            
            for elem in counter:
                if counter[elem]>0:
                    comb.append(elem)
                    counter[elem] -= 1
                    
                    permute(comb, counter)
                    
                    comb.pop()
                    counter[elem] += 1
            
        permute([], Counter(nums))
        return result