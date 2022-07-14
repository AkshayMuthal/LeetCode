# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, lsum):
        if node:
            if node.left:
                if node.left.left == None and node.left.right == None:
                    lsum += node.left.val
                else:
                    lsum = self.dfs(node.left, lsum)
            if node.right:
                lsum = self.dfs(node.right, lsum)
        return lsum
    
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)