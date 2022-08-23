class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        rl, cl = len(board), len(board[0])
        
        def dfs(r, c, board, rl, cl):
            if board[r][c]!="O":
                return
            board[r][c] = '.'
            for i,j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0<=i<rl and 0<=j<cl and board[i][j] == 'O':
                    dfs(i, j, board, rl, cl)
        
        for i in range(rl):
            dfs(i, 0, board, rl, cl)
            dfs(i, cl-1, board, rl, cl)
        
        for i in range(cl):
            dfs(0, i, board, rl, cl)
            dfs(rl-1, i, board, rl, cl)
            
        for i in range(rl):
            for j in range(cl):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"
