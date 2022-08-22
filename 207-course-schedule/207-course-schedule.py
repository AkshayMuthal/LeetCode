class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_map = {}
        indegree = [0]*numCourses
            
        for c_after, c_before in prerequisites:
            adj_map[c_before] = adj_map.get(c_before, []) + [c_after]
            indegree[c_after] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.pop()
            if course in adj_map:
                for c_after in adj_map[course]:
                    indegree[c_after] -= 1
                    if indegree[c_after] == 0:
                        q.append(c_after)
        
        for i in indegree:
            if i != 0:
                return False
        return True