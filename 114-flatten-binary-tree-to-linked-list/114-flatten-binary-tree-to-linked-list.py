# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stk = []
        node = root
        prev = None
        
        while node or stk:
            # print(stk)
            if node.right:
                stk.append(node.right)
            if node.left:
                node.right = node.left
                node.left = None
                node = node.right
            elif stk:
                node.right = stk.pop()   
                node = node.right
            else:
                break
        
        return root
