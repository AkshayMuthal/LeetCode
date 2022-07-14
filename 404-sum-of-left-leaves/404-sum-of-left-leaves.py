# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, direction):
            if not node:
                return 0
            if not node.left and not node.right and direction:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)