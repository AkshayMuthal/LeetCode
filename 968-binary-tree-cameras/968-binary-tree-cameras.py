# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if node == None:
                return 2
            left, right = dfs(node.left), dfs(node.right)
            if left == 0 or right == 0:
                self.res+=1
                return 1
            return 2 if left == 1 or right == 1 else 0
        
        return self.res + 1 if dfs(root) == 0 else self.res
