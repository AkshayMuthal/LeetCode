# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def good(self, max_r, root):
        if root!=None:
            if root.val>=max_r:
                self.count+=1
            max_r = max(max_r, root.val)
            self.good(max_r, root.left)
            self.good(max_r, root.right)
    
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.good(-10000, root)
        return self.count