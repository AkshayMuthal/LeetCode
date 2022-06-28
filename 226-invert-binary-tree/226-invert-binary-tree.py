# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        q = deque()
        q.append(root)
        
        while q:
            temp = q.popleft()
            left = temp.left
            temp.left = temp.right
            temp.right = left
            
            if temp.right!=None:
                q.append(temp.right)
            if temp.left!=None:
                q.append(temp.left)
        
        return root