class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i : [] for i in range(numCourses)}

        for edges in prerequisites:
            parent, child = edges[1], edges[0]

            adjList[parent].append(child)
        
        visited = set()
        def dfs(node):

            if node in visited:
                return False
            
            if len(adjList[node]) == 0:
                return True
            
            visited.add(node)

            for child in adjList[node]:

                if not dfs(child): return False
            
            visited.remove(node)
            adjList[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

