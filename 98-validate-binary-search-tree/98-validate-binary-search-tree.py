# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution(object):    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_valid(node, minv, maxv):
            if node == None:
                return True
            if minv >= node.val or node.val >= maxv:
                return False
            return check_valid(node.left, minv, node.val) and check_valid(node.right, node.val, maxv)
        return check_valid(root, -sys.maxint, sys.maxint)