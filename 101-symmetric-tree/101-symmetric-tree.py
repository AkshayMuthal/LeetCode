# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_sym(left, right):
            if left==None and right==None:
                return True
            if (left!=None and right==None) or (right!=None and left==None) or (left.val != right.val):
                return False
            return True and check_sym(left.left, right.right) and check_sym(left.right, right.left)
        return check_sym(root.left, root.right)