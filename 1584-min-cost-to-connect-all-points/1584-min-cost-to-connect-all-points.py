import sys

class Solution:
    def man_dist(self, p1, p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes = len(points)
        heap = [(0, 0)]
        min_dist = 0
        visited = [False]*nodes
        edges = 0
        
        while edges<nodes:
            weight, node = heapq.heappop(heap)
            if visited[node]:
                continue
            edges+=1
            min_dist+=weight
            visited[node] = True
            
            for next_node in range(nodes):
                if not visited[next_node]:
                    dist = self.man_dist(points[node], points[next_node])
                    heapq.heappush(heap, (dist, next_node))
                
        return min_dist