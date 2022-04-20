# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        if self.prev!=None and node.val<self.prev.val:
            if self.first == None:
                self.first = self.prev
            self.second = node
        self.prev = node
        self.inorder(node.right)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, None
        
        if root == None:
            return None
        self.inorder(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        return root