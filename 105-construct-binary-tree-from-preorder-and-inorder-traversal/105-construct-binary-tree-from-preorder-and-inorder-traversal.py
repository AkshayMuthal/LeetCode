# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        in_hm = {}
        for i in range(len(inorder)):
            in_hm[inorder[i]] = i
        
        self.ind = 0
        def traverse(l_ind, r_ind, preorder, inorder):
            if l_ind > r_ind or self.ind >= len(preorder):
                return None
            
            node = TreeNode(preorder[self.ind])
            self.ind += 1
            
            node_ind = in_hm[node.val]
            node.left = traverse(l_ind, node_ind-1, preorder, inorder)
            node.right = traverse(node_ind+1, r_ind, preorder, inorder)
            return node
        
        return traverse(0, len(inorder)-1, preorder, inorder)