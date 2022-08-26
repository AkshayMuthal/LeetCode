class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(ind, arr, ans):
            if ind == len(arr)-1:
                ans.append(arr)
            for i in range(ind, len(arr)):
                new_nums = arr.copy()
                new_nums[ind], new_nums[i] = new_nums[i], new_nums[ind]
                dfs(ind+1, new_nums, ans)
        
        ans = []
        dfs(0, nums, ans)
        return ans