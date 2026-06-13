class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if len(edges) == 0:
            return n

        adjList = {i : [] for i in range(n)}

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        visited = set()
        
        def bfs(node):

            q = collections.deque()
            q.append(node)
            visited.add(node)

            while q:

                currNode = q.popleft()

                for nei in adjList[currNode]:
                    if nei in visited:
                        continue
                    q.append(nei)
                    visited.add(nei)
        
        res = 0
        
        for node in range(n):
            if node not in visited:
                bfs(node)
                res+=1
        
        return res
                
            
        
