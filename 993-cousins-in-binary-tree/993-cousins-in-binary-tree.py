# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def height(node, target, parent):
            if node == None:
                return [None, None]
            if node.val == target:
                return [0, parent]
            ltup = height(node.left, target, node)
            if ltup[0]!=None:
                ltup[0]+=1
                return ltup
            rtup = height(node.right, target, node)
            if rtup[0]!=None:
                rtup[0] += 1
                return rtup
            return None, None
        
        xtup = height(root, x, None)
        ytup = height(root, y, None)
        if xtup[0] == ytup[0] and xtup[1]!=ytup[1]:
            return True
        return False