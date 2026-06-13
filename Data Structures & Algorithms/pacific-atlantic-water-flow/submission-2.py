class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        pac, atl = set(), set()
        
        def dfs(r,c,visit,preVal):
            if (r,c) in visit or r < 0  or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < preVal:
                return
            
            visit.add((r,c))

            for dr, dc in directions:
                dfs(r+dr, c + dc, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        res = []


        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) in pac and (row,col) in atl:
                    res.append((row,col))
        
        return res
