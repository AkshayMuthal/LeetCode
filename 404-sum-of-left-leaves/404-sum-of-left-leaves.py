# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, direction):
        if not node:
            return 0
        if not node.left and not node.right and direction:
            return node.val
        return self.dfs(node.left, True) + self.dfs(node.right, False)
    
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, False)