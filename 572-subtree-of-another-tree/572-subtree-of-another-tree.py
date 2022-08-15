# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSame(self, p, q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        return (p.val == q.val) and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)  
    
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        if root.val == subRoot.val and self.isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
