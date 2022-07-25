class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rm = [set() for _ in range(9)]
        cm = [set() for _ in range(9)]
        bm = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                bi = (i//3)*3 + j//3
                if val in rm[i] or val in cm[j] or val in bm[bi]:
                    return False
                rm[i].add(val)
                cm[j].add(val)
                bm[bi].add(val)
                
        return True