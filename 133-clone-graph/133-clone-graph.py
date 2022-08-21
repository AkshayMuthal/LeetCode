"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        hm = {node.val:Node(node.val)}
        q = deque([node])
        
        while q:
            curr = q.popleft()
            clone = hm[curr.val]
            
            for neighbor in curr.neighbors:
                if neighbor.val not in hm:
                    hm[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                clone.neighbors.append(hm[neighbor.val])
        
        return hm[node.val]
