class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Solving using BFS

        if len(edges) >= n:
            return False
        
        # lets make an ajacency list

        adjList = {i : [] for i in range(n)}

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
        
        return dfs(0,-1) and len(visited) == n