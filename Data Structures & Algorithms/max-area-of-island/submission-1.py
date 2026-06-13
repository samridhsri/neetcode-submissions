class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()

        def bfsAreaCalc(r,c):
            area = 0
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                area+=1

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if(nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0 or (nr, nc) in visited):
                        continue
                    q.append((nr,nc))
                    visited.add((nr, nc))
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfsAreaCalc(r,c))
        
        return maxArea