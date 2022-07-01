# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        ans = []
        level = [root]
        
        while level:
            ans.append([elem.val for elem in level])
            lr_pair = [(elem.left, elem.right) for elem in level]
            level = [elem for lr in lr_pair for elem in lr if elem]

        return ans
            