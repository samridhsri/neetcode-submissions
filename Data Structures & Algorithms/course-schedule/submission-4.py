class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Return true if it is possible to complete all the courses

        # Make an adjacency list
        adjList = {i : [] for i in range(numCourses)}

        for edge in prerequisites:
            parent = edge[1]
            child = edge[0]
            adjList[parent].append(child)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            
            if adjList[node] == []:
                return True
            
            visited.add(node)

            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            
            visited.remove(node)
            adjList[node] = []
            return True
        
        for curs in range(numCourses):
            if not dfs(curs): return False
        
        return True
