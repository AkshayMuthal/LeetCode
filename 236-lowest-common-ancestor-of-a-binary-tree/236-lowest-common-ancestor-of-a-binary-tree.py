# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_lca(self, root, p, q):
        if root == None:
            return False
        
        root_flag = False
        
        if root == p or root == q:
            root_flag = True
        
        left = self.get_lca(root.left, p, q)
        right = self.get_lca(root.right, p, q)
        
        if (left and right) or (left and root_flag) or (right and root_flag):
            self.ans = root
        
        return root_flag or left or right
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        self.get_lca(root, p, q)
        return self.ans