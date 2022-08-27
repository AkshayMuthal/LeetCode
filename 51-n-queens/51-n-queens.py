class Solution(object):
    def append_board(self, board, n, ans):
        temp = []
        for i in range(n):
            s = ""
            for j in range(n):
                if board[i][j] == 1:
                    s += "Q"
                else:
                    s += "."
            temp.append(s)
        ans.append(temp)
    
    def check(self, row, col, board, n):
        for i in range(n):
            if board[i][col]:
                return False
        j=col
        for i in range(row, -1, -1):
            if j<0:
                break
            if board[i][j]:
                return False
            j-=1
        
        j=col
        for i in range(row, -1, -1):
            if j>=n:
                break
            if board[i][j]:
                return False
            j+=1
        return True
    
    def solve(self, row, board, n, ans):
        if row == n:
            self.append_board(board, n, ans)

        for col in range(n):
            if self.check(row, col, board, n):
                board[row][col] = 1
                flag = self.solve(row+1, board, n, ans)
                board[row][col] = 0
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = [[0]*n for _ in range(n)]
        self.solve(0, board, n, ans)
        return ans