class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # If cycle -> False
        # Else -> True

        # create an adjacency list

        adjList = {i : [] for i in range(numCourses)}
        for edge in prerequisites:
            parent, child = edge[0], edge[1]

            adjList[parent].append(child)
        

        # Lets try with DFS
        visited = set()

        def dfs(curs):

            if curs in visited:
                return False

            if adjList[curs] == []:
                return True
            
            visited.add(curs)

            for nei in adjList[curs]:
                if not dfs(nei):
                    return False
            
            visited.remove(curs)
            adjList[curs] = []
            return True


        for curs in range(numCourses):
            if not dfs(curs): return False
        
        return True
