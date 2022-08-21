"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def create_node(self, node, new_node, hm, visited):
        if node.val in visited:
            return
        visited.add(node.val)
        
        for neighbor in node.neighbors:
            hm[neighbor.val] = hm[neighbor.val] if neighbor.val in hm else Node(neighbor.val)
            new_node.neighbors.append(hm[neighbor.val])
        for i in range(len(node.neighbors)):
            self.create_node(node.neighbors[i], new_node.neighbors[i], hm, visited)
    
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        source = Node(node.val)
        hm = {}
        hm[source.val] = source
        visited = set()
        self.create_node(node, source, hm, visited)
        return source
