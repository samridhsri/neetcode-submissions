class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # bfs se try karte hai

        adjList = {i : [] for i in range(n)}

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def bfs(node, parent):

            visited = set()
            
            q = collections.deque()
            q.append((node, parent))

            visited.add(node)

            while q:
                curr, p = q.popleft()

                for nei in adjList[curr]:
                    if nei == p:
                        continue
                    
                    if nei in visited:
                        return False
                    
                    q.append((nei, curr))
                    visited.add(nei)
            
            if len(visited) == n:
                return True
            
            return False
            
        
        return bfs(0,-1)
                    