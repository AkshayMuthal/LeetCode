class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights)
        n = len(heights[0])
        
        p_visited = set()
        a_visited = set()
        
        def traverse(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0<=i<m and 0<=j<n and heights[i][j] >= heights[r][c]:
                    traverse(i, j, visited)
        
        for i in range(m):
            traverse(i, 0, p_visited)
            traverse(i, n-1, a_visited)
        
        for i in range(n):
            traverse(0, i, p_visited)
            traverse(m-1, i, a_visited)
        
        return list(p_visited & a_visited)
        