class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # change in row and col to go down, up, right, left
        ROW, COL = len(grid), len(grid[0])
        visited = set()



        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited.add((row,col))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if(nr < 0 or nr >= ROW or nc < 0 or nc >= COL or grid[nr][nc]=="0" or (nr, nc) in visited):
                        continue
                    
                    q.append((nr,nc))
                    visited.add((nr,nc))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        
        return islands