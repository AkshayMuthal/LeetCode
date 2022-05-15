# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def traverse(self, node, k, s):
        if node!=None:
            if node.left == None and node.right == None and k == 0:
                s+=node.val
            else:
                s = self.traverse(node.left, k-1, s)
                s = self.traverse(node.right, k-1, s)
        return s
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        height = self.get_height(root)
        return self.traverse(root, height-1, 0)
