class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for r in grid:
            for c in r:
                arr.append(c)
        
        l = len(arr)
        ans = []
        pos = l-k%l
        for item in range(pos, l):
            ans.append(arr[item])
        for item in range(pos):
            ans.append(arr[item])
        
        i=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = ans[i]
                i+=1
        
        return grid