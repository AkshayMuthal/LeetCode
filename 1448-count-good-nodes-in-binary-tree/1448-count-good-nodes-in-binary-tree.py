# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, node, count, max_val):
        if not node:
            return count
        if node.val >= max_val:
            max_val = node.val
            count += 1
        count = self.inorder(node.left, count, max_val)
        count = self.inorder(node.right, count, max_val)
        return count
    
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        return self.inorder(root, count, root.val)