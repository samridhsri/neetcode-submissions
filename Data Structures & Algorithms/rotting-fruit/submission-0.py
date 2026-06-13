class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = collections.deque()
        fresh = 0
        time = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh+=1
                
                if grid[row][col] == 2:
                    q.append((row,col))
        
        while q and fresh > 0:

            queueSize = len(q)
            for _ in range(queueSize):

                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh-=1
            time+=1
        
        return time if fresh==0 else -1
