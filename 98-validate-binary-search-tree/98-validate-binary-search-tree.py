# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution(object):
    def check_valid(self, node, minv, maxv):
        if node == None:
            return True
        if minv < node.val < maxv:
            return self.check_valid(node.left, minv, node.val) and self.check_valid(node.right, node.val, maxv)
        return False
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_valid(root, -sys.maxint, sys.maxint)