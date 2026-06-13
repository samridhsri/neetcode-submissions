class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # Bruteforce solution

        pacific = atlantic = False
        directions = [[1,0], [-1,0], [0,1],[0,-1]]

        ROW, COL = len(heights), len(heights[0])

        def dfs(r, c, preVal):
            # r,c -> row, column
            # preVal -> height of the previous cell

            nonlocal pacific, atlantic

            if r < 0 or c<0:
                pacific = True
                return
            
            if r>=ROW or c>=COL:
                atlantic = True
                return
            
            if heights[r][c] > preVal:
                return # Water cannot go uphill
            
            tmp = heights[r][c]
            heights[r][c] = float('inf')

            for dr, dc in directions:
                dfs(r + dr, c + dc, tmp)
                if pacific and atlantic:
                    break
            heights[r][c] = tmp
        
        res = []
        for r in range(ROW):
            for c in range(COL):
                pacific = False
                atlantic = False

                dfs(r,c,float('inf'))

                if pacific and atlantic:
                    res.append([r,c])
        return res