class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Return the number of islands

        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        for row in range(ROWS):
            for col in range(COLS):

                if grid[row][col] == "1":
                    bfs(row,col)
                    islands+=1
        
        return islands