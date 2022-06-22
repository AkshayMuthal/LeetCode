class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        m = defaultdict(set)
        for i in range(len(nums)):
            m[nums[i]].add(i)
        
        for i in m:
            for j in m:
                if i == j and len(m[i])<2:
                    continue
                target = -i-j
                if target in m:
                    if target == i and len(m[i])<2:
                        continue
                    if target == j and len(m[j])<2:
                        continue
                    if target == i == j and len(m[i])<3:
                        continue
                    ans.add(tuple(sorted([i, j, target])))
        return ans