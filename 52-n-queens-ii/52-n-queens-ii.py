import copy

class Solution:
    def visit_node(self, row, col, n, visited):
        visited[row][col] = 1
        
        for i in range(n):
            visited[i][col] = 1
            visited[row][i] = 1
        
        i, j = row, col
        while i<n and j<n:
            visited[i][j] = 1
            i+=1
            j+=1
        
        i, j = row, col
        while i>=0 and j>=0:
            visited[i][j] = 1
            i-=1
            j-=1
        
        i, j = row, col
        while i>=0 and j<n:
            visited[i][j] = 1
            i-=1
            j+=1
            
        i, j = row, col
        while j>=0 and i<n:
            visited[i][j] = 1
            i+=1
            j-=1
        
        return visited
            
    def set_queen(self, col, row, n, visited):
        visited = self.visit_node(row, col, n , visited)
        if row == n-1:
            self.count +=1
            return
        
        for i in range(n):
            if visited[row+1][i] == 0:
                new_visited = copy.deepcopy(visited)
                self.set_queen(i, row+1, n, new_visited)

    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        for col in range(n):
            visited = [[0 for _ in range(n)] for _ in range(n)]
            self.set_queen(col, 0, n, visited)
        
        return self.count