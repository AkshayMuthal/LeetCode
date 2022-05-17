# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def targetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original!=None and cloned!=None and self.ans == None:
            if original.val == target.val and original.val == cloned.val:
                self.ans = cloned
                return
            self.targetCopy(original.left, cloned.left, target)
            self.targetCopy(original.right, cloned.right, target)
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = None
        self.targetCopy(original, cloned, target)
        return self.ans
        