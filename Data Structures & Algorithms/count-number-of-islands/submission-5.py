class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0":
                        continue
                    
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row,col)
                    islands+=1
        
        return islands