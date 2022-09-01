# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, node, max_val):
        if not node:
            return
        if node.val >= max_val:
            max_val = node.val
            self.count += 1
        self.inorder(node.left, max_val)
        self.inorder(node.right, max_val)
    
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.inorder(root, root.val)
        return self.count