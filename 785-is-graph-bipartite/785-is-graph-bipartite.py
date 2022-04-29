class Solution:
    def check_visited_cdn(self, idx, color):
        if self.color[idx] != color:
            self.stop = True
        
    def traverse(self, idx, graph, color):
        if self.stop:
            return
        
        if not self.visited[idx]:
            self.color[idx] = color
            self.visited[idx] = True
            queue = deque()
            
            for adj in graph[idx]:
                if not self.visited[adj]:
                    queue.append(adj)
                
                if self.color[adj]==-1:
                    self.color[adj] = color^1
                else:
                    self.check_visited_cdn(idx, color)
            
            while queue:
                self.traverse(queue.popleft(), graph, color^1)
                                
        else:
            self.check_visited_cdn(idx, color)
                
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.nodes = len(graph)
        self.visited = [False for i in range(self.nodes)]
        self.color = [-1 for i in range(self.nodes)]
        self.stop = False
        
        color = 0
        for i in range(self.nodes):
            if not self.visited[i]:
                if self.color[i]==-1:
                    color = color^1
                    self.traverse(i, graph, color)
                else:
                    self.traverse(i, graph, self.color[i])
        return not self.stop