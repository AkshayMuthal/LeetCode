# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -1001
        def inorder(root):
            if root == None:
                return 0

            left_sum = max(inorder(root.left), 0)
            right_sum = max(inorder(root.right), 0)

            self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)

            return root.val + max(left_sum, right_sum)
        
        inorder(root)
        return self.max_sum
