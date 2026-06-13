class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited.add((row,col))
            area = 0

            while q:
                r, c = q.popleft()
                area += 1

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if (nr < 0 or nr >= ROW or nc < 0 or nc >= COL or grid[nr][nc] == 0 or (nr,nc) in visited):
                        continue
                    
                    visited.add((nr,nc))
                    q.append((nr,nc))
            
            return area

        for r in range(ROW):
            for c in range(COL):

                if (grid[r][c] == 1 and ((r,c) not in visited)):
                    maxArea = max(bfs(r,c), maxArea)
        
        return maxArea
                    
        
        
