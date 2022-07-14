# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_hm = {}
        for i in range(len(inorder)):
            in_hm[inorder[i]] = i
        
        ind = 0
        
        def traverse(l_ind, r_ind, preorder, inorder):
            nonlocal ind
            
            if l_ind > r_ind or ind >= len(preorder):
                return None

            node = TreeNode(preorder[ind])
            ind += 1
            
            node_ind = in_hm[node.val]
            node.left = traverse(l_ind, node_ind-1, preorder, inorder)
            node.right = traverse(node_ind+1, r_ind, preorder, inorder)
            return node
        
        return traverse(0, len(inorder)-1, preorder, inorder)