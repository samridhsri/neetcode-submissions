class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        INF = 2147483647


        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            steps = 0
            visited = set()


            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    visited.add((r, c))

                    if grid[row][col] == 0:
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        
                        if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] != -1 and (nr,nc) not in visited:
                            q.append((nr, nc))
                            visited.add((nr,nc))
                steps += 1
            
            return INF
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
                            