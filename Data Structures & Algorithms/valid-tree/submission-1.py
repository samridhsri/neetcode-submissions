class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Solving using the dfs method

        adjList = {i : [] for i in range(n)}

        if (len(edges) >= n):
            return False
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        visited = set()
        
        def dfs(node, parent):

            if node in visited:
                return False
            
            visited.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False
            return True
            
        return dfs(0, -1) and n == len(visited)