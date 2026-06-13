class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def bfs(row, col):

            q = collections.deque()
            q.append((row,col))

            visited.add((row,col))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if(nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0" or (nr, nc) in visited):
                        continue
                    
                    q.append((nr,nc))
                    visited.add((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        
        return islands