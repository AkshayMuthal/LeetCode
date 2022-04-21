# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root):
        if root and self.ans==None:
            self.inorder(root.left)
            self.k-=1
            if self.k==0:
                self.ans = root
            self.inorder(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.k = k
        self.inorder(root)
        return self.ans.val