# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def k_small(node, k, ind):
            if self.ans != None:
                return self.ans
            if not node:
                return ind
            
            ind = k_small(node.left, k, ind) + 1
            if self.ans != None:
                return self.ans
            
            if ind == k:
                self.ans = node.val
                return self.ans
            
            return k_small(node.right, k, ind)
        
        self.ans = None
        return k_small(root, k, 0)
        